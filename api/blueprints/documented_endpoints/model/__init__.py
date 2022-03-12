from flask_restplus import Namespace, Resource, fields
from sqlalchemy import true
from config import mapping
import pandas as pd
import pickle
from hook import requests_search, requests_movie

namespace = Namespace("model", "Model related endpoint")
namespace2 = Namespace("movie", "Movie related endpoint")

payload = namespace.model(
    "model",
    {
        "movie_id": fields.Integer(
            description="The movie id that you want to predict the success of",
            required=True,
        ),
    },
)


@namespace2.route("/movie/<string:movie_name>")
class getmovie(Resource):
    @namespace2.response(200, "Success")
    def get(self, movie_name):
        """ Get the movie you want to predict the success of """
        output = requests_search(movie_name)
        return output


@namespace.route("/SVC")
class Model_SVC(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """Predict the class of the movie with SVC"""
        payload = namespace.payload
        inputs = requests_movie(int(payload["movie_id"]))
        filename = "../models/model_svc.pkl"
        with open(filename, "rb") as file:
            model = pickle.load(file)
        x = pd.DataFrame(inputs["response"], index=["0"])
        x = pd.DataFrame(inputs["response"], index=["0"])
        x.drop(columns=["movie_id", "title"], inplace=True)
        pred = model.predict(x)
        output = {"response": {inputs["response"]["title"]: mapping.PREDICTION_MAP[str(pred[0])]}}
        return output

@namespace.route("/XGBOOST")
class Model_SVC(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """Predict the class of the movie with XGBOOST"""
        payload = namespace.payload
        inputs = requests_movie(int(payload["movie_id"]))
        filename = "../models/model_xg_grid.pkl"
        with open(filename, "rb") as file:
            model = pickle.load(file)
        x = pd.DataFrame(inputs["response"], index=["0"])
        x = pd.DataFrame(inputs["response"], index=["0"])
        x.drop(columns=["movie_id", "title"], inplace=True)
        pred = model.predict(x)
        output = {"response": {inputs["response"]["title"]: mapping.PREDICTION_MAP[str(pred[0])]}}
        return output