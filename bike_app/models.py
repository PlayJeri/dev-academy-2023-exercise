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