from unicodedata import category
from flask import render_template,request,redirect,url_for,abort
from . import main

from ..models import User,Note
from .forms import PitchForm
from flask_login import login_required,current_user
from .. import db




# Views
@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        note = Note(data =pitch_form.pitch.data,category=pitch_form.Category.data)
        db.session.add(note)
        db.session.commit()

   
    return render_template('home.html',pitch_form=pitch_form)



