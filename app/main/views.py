from flask import render_template,request,redirect,url_for,abort
from . import main

from ..models import User
from .forms import PitchForm
from flask_login import login_required,current_user
# from .. import db,photos




# Views
@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
 
    '''
    View root page function that returns the home page and its data
    '''

   
    return render_template('home.html')



