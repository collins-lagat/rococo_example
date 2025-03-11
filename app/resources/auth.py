import os
from rococo.auth.tokens import generate_confirmation_token
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
        return {"message": "User logged in!"}


class ResetPassword(Resource):
    def post(self):
        return {"message": "Password reset!"}
