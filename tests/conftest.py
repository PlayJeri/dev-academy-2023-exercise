import pytest
from dotenv import load_dotenv
import os

from bike_app import create_app, db
load_dotenv(os.path.join(os.path.dirname(__file__),'..', '.env'))

@pytest.fixture()
def app():
    app = create_app('sqlite:///city_bike.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    with app.app_context():
        db.create_all()

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()