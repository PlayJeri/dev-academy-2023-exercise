from .extensions import db
from flask_login import UserMixin

class Rides(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departure_time = db.Column(db.DateTime)
    return_time = db.Column(db.DateTime)
    departure_station_id = db.Column(db.Integer)
    departure_station_name = db.Column(db.String)
    return_station_id = db.Column(db.Integer)
    return_station_name = db.Column(db.String)
    covered_distance_meters = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)


class Stations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.Integer, unique=True)
    station_name_finnish = db.Column(db.String)
    station_name_swedish = db.Column(db.String)
    station_name_english = db.Column(db.String)
    address_finnish = db.Column(db.String)
    address_swedish = db.Column(db.String)
    city_finnish = db.Column(db.String, nullable=True)
    city_swedish = db.Column(db.String, nullable=True)
    operator = db.Column(db.String, nullable=True)
    capacity = db.Column(db.Integer)
    x_coordinate = db.Column(db.Float)
    y_coordinate = db.Column(db.Float)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
