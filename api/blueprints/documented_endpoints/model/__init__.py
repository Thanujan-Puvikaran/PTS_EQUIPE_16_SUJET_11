from flask_restplus import Namespace, Resource, fields
from config import raiseError
import pickle
from flask import send_file
from hook import find_file, requests_search
import pandas as pd

namespace = Namespace("model", "Model related endpoints")

payload = namespace.model(
    "model",
    {
        "movie_name": fields.String(
            description="The movie that you want to predict the success of",
            required=False,
        ),
    },
)


@namespace.route("/NAME")  # REPLACE NAME WITH THE CORRECT NAME OF MODEL
class Model(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """Predict the class of the movie with NAME"""  # REPALCE NAME WITH THE CORRECT NAME OF MODEL
        try:

            payload = namespace.payload
            # filename = "../../../models/model.pkl"
            # with open(filename, "rb") as file:
            #     model = pickle.load(file)
            output = requests_search(payload["movie_name"])
            return output
            # payload = pd.DataFrame(payload.value, index=["0"])
            # pred = model.predict(payload)
            # output = {"response": "success"}
            # output = {"response": pred[0]}
            # return output
        except Exception as e:
            if raiseError.JSONERROR in e.__str__():
                return {"response": {"error": raiseError.JSONMESSAGE}}
            elif raiseError.TYPEERROR in e.__str__():
                return {"response": {"error": raiseError.TYPEMESSAGE}}
