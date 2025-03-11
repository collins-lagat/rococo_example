from flask_restful import Resource


class Register(Resource):
    def post(self):
        return {"message": "User registered!"}


class Login(Resource):
    def post(self):
        return {"message": "User logged in!"}


class ResetPassword(Resource):
    def post(self):
        return {"message": "Password reset!"}
