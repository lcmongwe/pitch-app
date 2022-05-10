from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):

    
    Category = SelectField(u'Category', choices=[('memes'), ('thought'), ('religious'),('motivational')])
    pitch = TextAreaField('Pitch', validators=[InputRequired()])
    submit = SubmitField('Submit')

