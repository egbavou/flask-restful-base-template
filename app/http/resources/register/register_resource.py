from flask import Response
from flask_restful import Resource
from flask import request, make_response
from app.http.controllers.register.register_controller import check_username, check_email, register


class RegisterResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = register(request, input_data)
        return make_response(response, status)
   
class CheckUsernameResource(Resource):
    @staticmethod
    def get() -> Response:
        input_data = request.args
        response, status = check_username(request, input_data)
        return make_response(response, status)
    
class CheckEmailResource(Resource):
    @staticmethod
    def get() -> Response:
        input_data = request.args
        response, status = check_email(request, input_data)
        return make_response(response, status)