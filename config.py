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
    SQLALCHEMY_DATABASE_WRITE = env.get("SQLALCHEMY_DATABASE_WRITE")
    SQLALCHEMY_DATABASE_READ = env.get("SQLALCHEMY_DATABASE_READ")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE=30
    SQLALCHEMY_POOL_TIMEOUT=300
    
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 3600,
        'pool_timeout': 30,
        'pool_pre_ping': True,
        'pool_size': 10,
        'isolation_level': 'READ UNCOMMITTED'
    }
    
    SQLALCHEMY_BINDS = {
        'slaves': env.get("SQLALCHEMY_DATABASE_READ")
    }
    
    #JWT
    JWT_SECRET_KEY = env.get("JWT_SECRET")
    JWT_ALGO = env.get("JWT_ALGO")
    
    #AWS
    SQS_QUEUE_URL = env.get('SQS_QUEUE_URL')
    AWS_ACCESS_KEY_ID = env.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env.get('AWS_SECRET_ACCESS_KEY')
    AWS_DEFAULT_REGION = env.get('AWS_DEFAULT_REGION')
    
    #REDIS
    REDIS_HOST = env.get('REDIS_HOST')
    REDIS_PORT = env.get('REDIS_PORT')
    REDIS_URL = env.get('REDIS_URL')
    REDIS_USERNAME_DB = env.get('REDIS_USERNAME_DB')
    REDIS_MAIL_DB = env.get('REDIS_MAIL_DB')
    REDIS_PHONE_DB = env.get('REDIS_PHONE_DB')
    REDIS_USERS_DB = env.get('REDIS_USERS_DB ')
    REDIS_TOKEN_DB = env.get('REDIS_TOKEN_DB')
    
    #CELERY
    CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND')
    CELERY_RESULT_BROKER = env.get('CELERY_RESULT_BROKER')
    BROKER_TRANSPORT_OPTIONS = {
        'region': env.get('AWS_DEFAULT_REGION'),
        'predefined_queues': {
            'celery': {
                'url': env.get('SQS_QUEUE_URL'),
                'access_key_id': env.get('AWS_ACCESS_KEY_ID'),
                'secret_access_key': env.get('AWS_SECRET_ACCESS_KEY'),
                'backoff_policy': {1: 10, 2: 20, 3: 40, 4: 80, 5: 320, 6: 640},

            }
        },
        #'polling_interval': 5,  # number of sec to sleep between polls
        'wait_time_seconds': 5
    }
    
    #SMS KEY
    SMS_API_KEY = env.get('SMS_API_KEY')
    
    ATATUS_KEY = env.get('ATATUS_KEY')
    ATATUS_PROJECT = env.get('ATATUS_PROJECT')
    
    MEDIA_CDN_URL = env.get('MEDIA_CDN_URL')
    HLS_CDN_URL = env.get('HLS_CDN_URL')
    THUNBNAIL_CDN_URL = env.get('THUNBNAIL_CDN_URL')
    

class EmailConfig:
    
    EMAIL_API_KEY= env.get('EMAIL_API_KEY')
    EMAIL_SENDER_NAME= env.get('EMAIL_SENDER_NAME')
    EMAIL_SENDER= env.get('EMAIL_SENDER')