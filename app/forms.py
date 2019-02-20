from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired

class Uploadr(FlaskForm):
    fyle = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], message='Images only!')
    ])