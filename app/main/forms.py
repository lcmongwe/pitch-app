from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
	title = StringField('Title', validators=[InputRequired()])
	description = TextAreaField("write your pitch here",validators=[InputRequired()])
	category = SelectField('categories', choices=[ ('memes','memes'), ('thought','thought'),('religious','religious'),('motivational','motivational')],validators=[InputRequired()])
	submit = SubmitField('Submit')

# class PitchForm(FlaskForm):
#     Category = SelectField(u'Category', choices=[('memes'), ('thought'), ('religious'),('motivational')])
#     pitch = TextAreaField('Pitch', validators=[InputRequired()])
#     submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[InputRequired()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()