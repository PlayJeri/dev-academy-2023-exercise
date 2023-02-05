from flask import Flask, Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from .extensions import db
from .models import Users
from .forms import LoginForm, CreateStationForm
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('auth.admin'))
        else:
            flash('username or password wrong!', 'danger')

    return render_template('login.html', form=form)



@auth.route('/admin')
@login_required
def admin():



    return render_template('admin.html')


@auth.route('/addStation', methods=['GET', 'POST'])
@login_required
def add_station():

    form = CreateStationForm()


    return render_template('addStation.html', form=form)