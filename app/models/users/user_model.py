"""Data models."""
import datetime
from flask_sqlalchemy import SQLAlchemy
from db import db


# The User class is a data model for user accounts
class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255), index=True, nullable=False)
    first_name = db.Column(db.String(255), index=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(80), index=True, nullable=True)
    phone_number = db.Column(db.String(80), index=True, unique=True, nullable=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.last_name = kwargs.get("last_name")
        self.first_name = kwargs.get("first_name")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.phone_number = kwargs.get("phone_number")
        self.age = kwargs.get("age")
        
    def json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'age': self.age,
            'email': self.email,
            'phone_number': self.phone_number,
            'created': self.created
        }

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<User {}>".format(self.username)