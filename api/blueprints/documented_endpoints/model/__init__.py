from unicodedata import name
from flask_restplus import Namespace, Resource, fields
from sqlalchemy import true
from config import raiseError

# import pickle
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


@namespace.route("/NAME")  # REPLACE NAME WITH THE CORRECT NAME OF MODEL
class Model(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """Predict the class of the movie with NAME"""  # REPALCE NAME WITH THE CORRECT NAME OF MODEL
        try:
            payload=namespace.payload
            input = requests_movie(payload["movie_id"])
            # filename = "../../../models/model.pkl"
            # with open(filename, "rb") as file:
            #     model = pickle.load(file)
            # payload = pd.DataFrame(payload.value, index=["0"])
            # pred = model.predict(input)
            output = {"response": "success"}
            # output = {"response": pred[0]}
            return output
        except Exception as e:
            if raiseError.JSONERROR in e.__str__():
                return {"response": {"error": raiseError.JSONMESSAGE}}
            elif raiseError.TYPEERROR in e.__str__():
                return {"response": {"error": raiseError.TYPEMESSAGE}}
