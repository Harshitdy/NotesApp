from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    # this below is called as one-to-many, because one user can have many notes
    # Note:- but you can ony refer to a primary key of the user as you can see below
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # if we want a user can see all of their notes so for that you have to 
    # create a relationship between user and his notes
    # Note:- This should be in capital
    notes = db.relationship('Note') # this is going to be a list