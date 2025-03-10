from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)
api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(HelloWorld, "/hello")
app.register_blueprint(api_bp)
