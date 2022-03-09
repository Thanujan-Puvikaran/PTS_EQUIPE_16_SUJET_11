from flask import Flask
from blueprints.documented_endpoints import blueprint as endpoint

app = Flask(__name__, template_folder="templates")
app.config.SWAGGER_UI_DOC_EXPANSION = "list"
app.config["RESTPLUS_MASK_SWAGGER"] = False
app.register_blueprint(endpoint)

app.run(debug=True)
