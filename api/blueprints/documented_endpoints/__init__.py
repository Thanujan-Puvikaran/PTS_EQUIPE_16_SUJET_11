from flask import Blueprint
from flask_restplus import Api
from blueprints.documented_endpoints.model import namespace as models_ns
from blueprints.documented_endpoints.model import namespace2 as movie_ns


blueprint = Blueprint("api", __name__, url_prefix="/v1")

api_extension = Api(
    blueprint,
    title="PTS EQUIPE 16 SUJET 11",
    version="1.0",
    description="Api to present the results of our model",
    doc="/documentation",
)

api_extension.add_namespace(movie_ns)
api_extension.add_namespace(models_ns)

