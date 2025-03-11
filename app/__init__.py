from flask import Flask, Blueprint
from flask_restful import Resource, Api
from app.resources.account import Account
from app.resources.auth import Register, Login, ResetPassword

app = Flask(__name__)
api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)


@app.route("/")
def App():
    return "<p>Vue App!</p>"


class Actuator(Resource):
    def get(self):
        return {"db_version": 1, "api_version": 1}


api.add_resource(Actuator, "/version")
api.add_resource(Account, "/account")
api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(ResetPassword, "/reset-password")

app.register_blueprint(api_bp)
