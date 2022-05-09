from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):

    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Movie review', validators=[InputRequired()])
    submit = SubmitField('Submit')

class YourPitch(FlaskForm):
    bio = TextAreaField('write your pitch here.',validators = [InputRequired()])
    submit = SubmitField('Submit')