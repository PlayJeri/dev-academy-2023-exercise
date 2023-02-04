from flask import Blueprint, render_template, redirect, url_for, request, flash
from .extensions import db
from .models import Rides, Stations


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
            ).paginate(per_page=50, page=page_num, error_out=True)
    elif sort_order == 'asc':
        rides = Rides.query.order_by(
            Rides.covered_distance_meters.asc()
            ).paginate(per_page=50, page=page_num, error_out=True)
    else:
        rides = Rides.query.paginate(per_page=50, page=page_num, error_out=True)

    return render_template('rides.html', rides=rides)


@views.route('/stations/<int:page_num>', methods=['GET', 'POST'])
def stations(page_num):
    stations = Stations.query.paginate(per_page=50, page=page_num, error_out=True)



    return render_template('stations.html', stations=stations)


@views.route('/station/<int:station_id>')
def station(station_id):
    station = Stations.query.filter_by(id=station_id).first()

    return render_template('station.html', station=station)


@views.route('/search', methods=['POST'])
def search():
    search_item = request.form.get("search").capitalize()
    print(search_item)
    station = Stations.query.filter_by(
            station_name_finnish=search_item).first()
    
    if not station:
        flash('not found')
        return redirect(url_for('views.stations', page_num=1))
    return redirect(url_for('views.station', station_id=station.id))
