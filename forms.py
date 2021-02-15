from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, Email, Optional


class AddCupCake(FlaskForm):
    flavor = StringField("flavor", validators=[
        InputRequired(message="Flavor can't be blank")
    ])
    size = StringField("size", validators=[
        InputRequired(message="size can't be blank")
    ])
    image = StringField("image")
    rating = FloatField("rating")

