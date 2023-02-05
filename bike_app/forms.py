from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


class CreateStationForm(FlaskForm):
    station_id = IntegerField('station id', validators=[DataRequired()])
    station_name_finnish = StringField('station name finnish', validators=[DataRequired()])
    station_name_swedish = StringField('station name swedish')
    station_name_english = StringField('station name english')
    address_finnish = StringField('station address in finnish', validators=[DataRequired()])
    address_swedish = StringField('station address in swedish')
    city_finnish = StringField('city name finnish', validators=[DataRequired()])
    city_swedish = StringField('city name swedish')
    operator = StringField('operator')
    capacity = IntegerField('station capacity')
    x_coordinate = FloatField('station x coordinates', validators=[DataRequired()])
    y_coordinate = FloatField('station y coordinates', validators=[DataRequired()])
    submit = SubmitField('submit')