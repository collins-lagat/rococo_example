import os
from rococo.auth.tokens import (
    generate_access_token,
    generate_confirmation_token,
    validate_confirmation_token,
)
from uuid import UUID

from flask import request
from flask_restful import Resource
from rococo.messaging import RabbitMqConnection
from rococo.models.email import Email
from rococo.models.login_method import LoginMethod
from rococo.models.organization import Organization
from rococo.models.otp_method import OtpMethod
from rococo.models.person import Person
from rococo.models.person_organization_role import PersonOrganizationRole
from rococo.models.recovery_code import RecoveryCode

from app.repositories.email import EmailRepository
from app.repositories.factory import RepositoryFactory
from app.repositories.organization import OrganizationRepository
from app.repositories.otp_method import OtpMethodRepository
from app.repositories.person import PersonRepository
from app.repositories.person_organisation_role import PersonOrganizationRoleRepository
from app.repositories.recovery_code import RecoveryCodeRepository
from app.repositories.login_method import LoginMethodRepository


class Register(Resource):
    def post(self):
        temp_id = UUID(int=1, version=4)
        data = request.get_json()

        # Check if user already exists
        email_repo = RepositoryFactory.get_repository(EmailRepository)
        email = email_repo.get_one({"email": data.get("email")})

        if email:
            return {"message": "User already exists"}

        # Organization
        organization = Organization(name=f"{data.get('first_name')}'s Organization")
        organization.prepare_for_save(changed_by_id=temp_id)
        org_repo = RepositoryFactory.get_repository(OrganizationRepository)
        org_repo.save(organization)

        # Person
        person = Person(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
        )
        person.prepare_for_save(changed_by_id=temp_id)
        person_repo = RepositoryFactory.get_repository(PersonRepository)
        person_repo.save(person)

        # Add User to Organization
        person_organization_role = PersonOrganizationRole(
            person=person.entity_id, organization=organization.entity_id, role="admin"
        )
        person_organization_role.prepare_for_save(changed_by_id=temp_id)
        person_organization_role_repo = RepositoryFactory.get_repository(
            PersonOrganizationRoleRepository
        )
        person_organization_role_repo.save(person_organization_role)

        # Email
        email = Email(
            person=person.entity_id,
            email=data.get("email"),
            is_verified=True,
            is_default=True,
        )
        email.prepare_for_save(changed_by_id=temp_id)
        email_repo.save(email)

        # Send Reset Password Email
        # 1. Create OTP Method
        otp_method = OtpMethod(person=person.entity_id, secret="super-secret")
        otp_method.prepare_for_save(changed_by_id=temp_id)
        otp_method_repo = RepositoryFactory.get_repository(OtpMethodRepository)
        otp_method_repo.save(otp_method)
        # 2. Create Recovery Code
        recovery_code = RecoveryCode(
            otp_method=otp_method.entity_id, secret="super-secret"
        )
        recovery_code.prepare_for_save(changed_by_id=temp_id)
        recovery_code_repo = RepositoryFactory.get_repository(RecoveryCodeRepository)
        # recovery_code_repo.save(recovery_code, send_message=True)
        # HACK: send message manually
        # TODO: wait for upstream fix
        recovery_code_repo.save(recovery_code)
        # 3. Send Email
        with RabbitMqConnection(
            host=os.environ.get("RABBITMQ_HOST", "localhost"),
            port=int(os.environ.get("RABBITMQ_PORT", "5672")),
            username=os.environ.get("RABBITMQ_USERNAME", "guest"),
            password=os.environ.get("RABBITMQ_PASSWORD", "guest"),
            virtual_host="/",
        ) as connection:
            connection.send_message(
                recovery_code_repo.queue_name,
                {
                    "base_url": request.base_url,
                    "token": generate_confirmation_token(
                        email.email, recovery_code.secret
                    ),
                },
            )

        return {"message": "User registered!"}


class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # Check if user exists
        email_repo = RepositoryFactory.get_repository(EmailRepository)
        email_obj = email_repo.get_one({"email": email})
        if not email_obj:
            return {"message": "User does not exist"}

        # Check if password is correct
        login_method_repo = RepositoryFactory.get_repository(LoginMethodRepository)
        login_method = login_method_repo.get_one(
            {"person": email_obj.person, "email": email_obj.entity_id}
        )

        if not login_method:
            return {"message": "Invalid email or password"}

        if login_method.method_type == "password":
            if login_method.method_data != password:
                return {"message": "Invalid email or password"}
            else:
                auth_token, expiry = generate_access_token(
                    email_obj.person, "super-secret", 3600
                )
                return {
                    "message": "User logged in!",
                    "auth_token": auth_token,
                    "expiry": expiry,
                }
        else:
            return {"message": "Invalid login method"}


class NewPassword(Resource):
    def post(self):
        temp_id = UUID(int=1, version=4)
        data = request.get_json()
        token = data.get("token")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        # Check if token is valid
        if not validate_confirmation_token(token, "super-secret", 3600):
            return {"message": "Invalid token"}

        # Check if passwords match
        if password != confirm_password:
            return {"message": "Passwords do not match"}

        # Save Password
        email = token.split(":")[0]
        email_repo = RepositoryFactory.get_repository(EmailRepository)
        email_obj = email_repo.get_one({"email": email})
        login_method_repo = RepositoryFactory.get_repository(LoginMethodRepository)
        login_method = LoginMethod(
            person=email_obj.person,
            method_type="password",
            method_data=password,
            email=email_obj.entity_id,
            password=password,
        )
        login_method.prepare_for_save(changed_by_id=temp_id)
        login_method_repo.save(login_method)

        # Clear Recovery Codes
        otp_method_repo = RepositoryFactory.get_repository(OtpMethodRepository)
        otp_method = otp_method_repo.get_one({"person": email_obj.person})
        recovery_code_repo = RepositoryFactory.get_repository(RecoveryCodeRepository)
        recovery_codes = recovery_code_repo.get_many(
            {"otp_method": otp_method.entity_id}
        )
        for recovery_code in recovery_codes:
            recovery_code_repo.delete(recovery_code)

        return {
            "message": "Password reset!",
        }
