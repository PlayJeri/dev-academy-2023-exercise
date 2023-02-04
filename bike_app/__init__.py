from flask import Flask
from .extensions import db
from .routes import views
from dotenv import load_dotenv
import os


def create_app():

    # App config
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///city_bike.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(views)

    return app

