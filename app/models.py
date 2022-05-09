# from email.policy import default
# from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime

class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


    def __repr__(self):
        return f'Note {self.data}'

class User(db.Model,UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), unique=True)
    pass_secure = db.Column(db.String(255))
    username = db.Column(db.String(255))
    notes = db.relationship('Note',backref = 'note',lazy="dynamic")

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'