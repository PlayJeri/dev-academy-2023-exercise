from bike_app.extensions import db
from bike_app.models import Rides
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