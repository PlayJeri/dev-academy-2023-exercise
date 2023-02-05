from flask import Flask
from .extensions import db, login_manager
from .routes import views
from dotenv import load_dotenv
import os


def create_app(database_uri='sqlite:///city_bike.db'):

    # App config
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(views)

    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app

