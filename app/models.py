# from email.policy import default
# from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# class Note(db.Model):
#     __tablename__ = 'note'

#     id = db.Column(db.Integer,primary_key = True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


#     # def __repr__(self):
#     #     return f'Note {self.username}'

class User(db.Model,UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    # notes = db.relatioship('Note')


#     # def __repr__(self):
#     #     return f'User {self.username}'