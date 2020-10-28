from flask import app, Flask

from config import Config
from links_transform.database import db_session

def create_app(config_class=Config):
    app = Flask(__name__,static_folder='static', static_url_path='')
    app.config.from_object(config_class)

