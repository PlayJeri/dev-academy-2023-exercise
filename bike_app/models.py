from .extensions import db

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
    station_id = db.Column(db.Integer)
    station_name_finnish = db.Column(db.String)
    station_name_swedish = db.Column(db.String)
    address_finnish = db.Columm(db.String)
    address_swedish = db.Columm(db.String)
    city_finnish = db.Column(db.String)
    city_swedish = db.Column(db.String)
    operator = db.Column(db.String)
    capacity = db.Column(db.Integer)
    x_coordinate = db.Column(db.Float)
    y_coordinate = db.Column(db.Float)
