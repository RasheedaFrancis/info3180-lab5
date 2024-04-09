# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired,DataRequired
from flask_wtf.file import FileField, FileAllowed,FileRequired


class MovieForm(FlaskForm):
    title= StringField('Title', validators=[InputRequired()])
    description= PasswordField('Description', validators=[InputRequired()])
    poster = FileField('Poster', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Only images allowed!')])