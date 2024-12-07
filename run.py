import os
from flask import Flask
from DXsystems_backend.api import api
from DXsystems_backend.api.config import config
import logging
from flask_cors import CORS

config_name=os.environ.get("CONFIG","local")

app=Flask(__name__)
CORS(app)
app.config.from_object(config[config_name])
app.logger.setLevel(logging.DEBUG)

app.register_blueprint(api)

if __name__=="__main__":
    app.run(debug=True)
