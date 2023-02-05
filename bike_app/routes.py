from flask import Blueprint, render_template, redirect, url_for, request, flash
from .extensions import db
from .models import Rides, Stations
from sqlalchemy import desc


views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template('home.html', url=url_for)


@views.route('/rides/<int:page_num>')
def rides(page_num):
    sort_order = request.args.get('sort', 'default')
    if sort_order == 'desc':
        rides = Rides.query.order_by(
            Rides.covered_distance_meters.desc()
            ).paginate(per_page=25, page=page_num, error_out=True)
    elif sort_order == 'asc':
        rides = Rides.query.order_by(
            Rides.covered_distance_meters.asc()
            ).paginate(per_page=25, page=page_num, error_out=True)
    else:
        rides = Rides.query.paginate(per_page=25, page=page_num, error_out=True)

    return render_template('rides.html', rides=rides)


@views.route('/stations/<int:page_num>', methods=['GET', 'POST'])
def stations(page_num):
    stations = Stations.query.paginate(per_page=50, page=page_num, error_out=True)

    return render_template('stations.html', stations=stations)


@views.route('/station/<int:station_id>')
def station(station_id):
    station = Stations.query.filter_by(id=station_id).first()
    started_rides = Rides.query.filter_by(departure_station_id=station_id).count()
    ended_rides = Rides.query.filter_by(return_station_id=station_id).count()

    top5_return_stations = (
        Rides.query
        .with_entities(Rides.return_station_name, db.func.count(Rides.return_station_id).label('count'))
        .filter(Rides.departure_station_id == station_id)
        .group_by(Rides.return_station_id)
        .order_by(desc('count'))
        .limit(5)
        .all()
    )
    top5_departure_stations = (
        Rides.query
        .with_entities(Rides.departure_station_name, db.func.count(Rides.departure_station_id).label('count'))
        .filter(Rides.return_station_id == station_id)
        .group_by(Rides.departure_station_id)
        .order_by(desc('count'))
        .limit(5)
        .all()
    )

    return render_template(
        'station.html', 
        station=station, 
        started_rides=started_rides, 
        ended_rides=ended_rides, 
        top5_returns=top5_return_stations,
        top5_departures=top5_departure_stations)


@views.route('/search', methods=['POST'])
def search():
    search_item = request.form.get("search").capitalize()
    print(search_item)
    station = Stations.query.filter_by(
            station_name_finnish=search_item).first()
    
    if not station:
        flash('Station not found', 'warning')
        return redirect(url_for('views.stations', page_num=1))
    return redirect(url_for('views.station', station_id=station.id))
