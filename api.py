
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from db import db
from app.http.resources.users.user_resource import UserResource, UserListApi
from app.exceptions.handler import handle_404_error, handle_500_error
# from flask import make_response

app = Flask(__name__)
config = Config()

app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
app.config['JWT_ALGO'] = Config.JWT_ALGO
jwt = JWTManager(app)

api = Api(app=app)

db.init_app(app)

with app.app_context():

    db.create_all()  # Create database tables for our data models

api.add_resource(UserResource, '/api/users','/api/users/<int:user_id>')
api.add_resource(UserListApi,"/api/users")

@app.errorhandler(404)
def handler(error):
    return handle_404_error(error)

@app.errorhandler(500)
def handlery(error):
    return handle_500_error(error)

if __name__ == '__main__':
    # TODO: Add swagger integration
    app.run(debug=True)  # important to mention debug=True
