"""Flask configuration variables."""
from os import environ as env, path
from os import path


from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = env.get("SECRET_KEY")
    FLASK_APP = env.get("FLASK_APP")
    FLASK_ENV = env.get("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = env.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #JWT
    JWT_SECRET_KEY = env.get("JWT_SECRET_KEY")
    JWT_ALGO = env.get("JWT_ALGO ")