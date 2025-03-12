import os
from dotenv import load_dotenv
from flask import Blueprint, Flask, send_file, send_from_directory
from flask_restful import Api, Resource

from app.resources.account import Account
from app.resources.auth import Login, Register, NewPassword

load_dotenv()

app = Flask(__name__)
api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)


@app.route("/")
def index():
    return send_file(os.path.join(app.root_path, "views/dist/index.html"))


@app.route("/<path:path>")
def dist(path):
    return send_from_directory(os.path.join(app.root_path, "views/dist"), path)


class Actuator(Resource):
    def get(self):
        return {"db_version": 1, "api_version": 1}


api.add_resource(Actuator, "/version")
api.add_resource(Account, "/account")
api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(NewPassword, "/new-password")

app.register_blueprint(api_bp)
