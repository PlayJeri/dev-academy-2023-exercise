from bike_app.extensions import db
from bike_app.models import Rides, Stations
from bike_app import create_app
from datetime import datetime
import csv

app = create_app()

date_format = "%Y-%m-%dT%H:%M:%S"

with app.app_context():
    with open('csv_files/2021-07.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        error_counter = 0
        for row in reader:
            try:
                if (int(row[6]) > 10) and (int(row[7]) > 10):
                    new_ride = Rides(
                        departure_time=datetime.strptime(row[0], date_format),
                        return_time=datetime.strptime(row[1], date_format),
                        departure_station_id=int(row[2]),
                        departure_station_name=row[3],
                        return_station_id=int(row[4]),
                        return_station_name=row[5],
                        covered_distance_meters=int(row[6]),
                        duration_seconds=int(row[7])
                        )
                    db.session.add(new_ride)
            except Exception as e:
                error_counter+=1
        print(f'{error_counter} rows of data discarded')        
        db.session.commit()


with app.app_context():
    with open('csv_files/asemat.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        error_counter = 0
        for row in reader:
            try:
                new_station = Stations(
                        station_id = int(row[1]),
                        station_name_finnish = row[2],
                        station_name_swedish = row[3],
                        station_name_english = row[4],
                        address_finnish = row[5],
                        address_swedish = row[6],
                        city_finnish = row[7],
                        city_swedish = row[8],
                        operator = row[9],
                        capacity = int(row[10]),
                        x_coordinate = float(row[11]),
                        y_coordinate = float(row[12]))
                db.session.add(new_station)
            except Exception as e:
                error_counter+=1
                print(e)
        print(f'{error_counter} rows of data discarded')
        db.session.commit()
            