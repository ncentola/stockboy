from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
# from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

# cors = CORS(app, resources={r"*": {"origins": "*"}})

db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app)

from app import resources, schemas, models, util_routes
