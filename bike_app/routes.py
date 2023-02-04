from flask import Blueprint, render_template, redirect, url_for
from .extensions import db
from .models import Rides


views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template('home.html', url=url_for)


@views.route('/rides/<int:page_num>')
def rides(page_num):
    rides = Rides.query.paginate(per_page=20, page=page_num, error_out=True)

    return render_template('index.html', rides=rides)