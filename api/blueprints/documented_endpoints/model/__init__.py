from flask_restplus import Namespace, Resource, fields
from numpy.core.fromnumeric import ndim
from config import raiseError
from mapping import defaultValue
import pickle
from flask import send_file
from hook import find_file
import pandas as pd

namespace = Namespace("model", "Model related endpoints")

payload = namespace.model(
    "model",
    {
        "Age": fields.Integer(
            description="Age: the value must be above 18, else there will be an error",
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
            # payload = defaultValue(payload=namespace.payload, flag=False)
            # knn_filename = "../model/knn.pkl"
            # with open(knn_filename, "rb") as file:
            #     knn_model = pickle.load(file)
            # payload = pd.DataFrame(payload.value, index=["0"])
            # pred = knn_model.predict(payload)
            output = {"response": "success"}
            # output = {"response": pred[0]}
            return output
        except Exception as e:
            if raiseError.JSONERROR in e.__str__():
                return {"response": {"error": raiseError.JSONMESSAGE}}
            elif raiseError.TYPEERROR in e.__str__():
                return {"response": {"error": raiseError.TYPEMESSAGE}}
