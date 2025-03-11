from flask_restful import Resource


class Account(Resource):
    def get(self):
        return {
            "entity_id": "1",
            "active": True,
            "first_name": "John",
            "last_name": "Doe",
        }
