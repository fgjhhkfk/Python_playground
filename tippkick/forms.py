from flask_wtf import FlaskForm
from wtforms import SubmitField


class ButtonForm(FlaskForm):
    button = SubmitField("1")
