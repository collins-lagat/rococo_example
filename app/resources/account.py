from flask import request
from flask_restful import Resource

from app.repositories.factory import RepositoryFactory
from app.repositories.person import PersonRepository


class Account(Resource):
    def get(self):
        person_repo = RepositoryFactory.get_repository(PersonRepository)
        person = person_repo.get_many()[0]
        return person.as_dict(convert_datetime_to_iso_string=True)
