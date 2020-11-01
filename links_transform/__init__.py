from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from config import Config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    ma.init_app(app)
    from links_transform.resources.links import LinksResource
    from links_transform.resources.links_stat import LinksStat
    api = Api(prefix='/api')
    api.add_resource(LinksResource, '/long_to_short',
                     '/<short_postfix>')
    api.add_resource(LinksStat, '/statistic/<short_postfix>')
    api.init_app(app)
    migrate.init_app(app, db)

    return app
