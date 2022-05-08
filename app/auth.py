from xmlrpc.client import boolean
from flask import Blueprint,render_template,request,flash,redirect,url_for
# from .models import User,Note
# from werkzeug.security import generate_password_hash,check_password_hash
# from . import db
# from flask_login import  login_user,logout_user,login_required,current_user

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    # if request.method=='POST':
    #     email=request.form.get('email')
    #     password=request.form.get('password')

    #     user=User.query.filter_by(email=email).first()
    #     if user:
    #         if check_password_hash(user.password,password):
    #             flash('logged in successfuly', category='success')
    #             login_user(user, remember='True')
    #             return redirect (url_for('views.home'))

    #         else:
    #             flash('incorrrect email/password, try again!', category='error')
    #     else:
    #         flash('emaail does not exist', category='error')

    return render_template("login.html")

@auth.route('/logout')
# @login_required
def logout():
    # logout_user()
    return redirect(url_for('login.html'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    # if request.method=='POST':
    #     email = request.form.get('email')
    #     first_name = request.form.get('firstName')
    #     password1 = request.form.get('password1')
    #     password2 = request.form.get('password2')

    #     user = User.query.filter_by(email=email).first()

    #     if user:
    #         flash('email exists',category='error')

    #     elif password1 != password2:
    #         flash('passwords dont match', category="error") 
        
    #     else:
    #         new_user = User(email=email,first_name=first_name,password=generate_password_hash(password1,method='sha256'))
    #         db.session.add(new_user)
    #         db.session.commit()
    #         login_user(user, remember='True')
    #         flash('account created', category='success')

    #         redirect(url_for('views.home'))

    return render_template("sign_up.html")