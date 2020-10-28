from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from config import Config

db = SQLAlchemy()
ma = Marshmallow()
api = Api()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    ma.init_app(app)
    from links_transform.links import LinksResource
    api.add_resource(LinksResource, '/')
    api.init_app(app)

    return app
