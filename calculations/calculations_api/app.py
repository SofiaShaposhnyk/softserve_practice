from flask import Flask
from .api_v1 import bp


app = Flask(__name__)
app.register_blueprint(bp)
