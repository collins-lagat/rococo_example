from flask import request
from flask_restful import Resource

from app.repositories.factory import RepositoryFactory
from app.repositories.person import PersonRepository
from rococo.auth.tokens import validate_access_token


class Account(Resource):
    def get(self):
        token = request.headers.get("Authorization")
        if not token:
            return {"message": "No token provided"}, 400
        entity_id = validate_access_token(token, "super-secret", 3600)
        if not entity_id:
            return {"message": "Unauthorized"}, 401
        person_repo = RepositoryFactory.get_repository(PersonRepository)
        person = person_repo.get_one({"entity_id": entity_id})
        data = person.as_dict(convert_datetime_to_iso_string=True)

        return {"data": data}
