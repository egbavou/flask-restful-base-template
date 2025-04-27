from flask import Response
from flask_restful import Resource
from flask import request, make_response
from app.http.controllers.users.user_controller import  send_reset_password_code, check_reset_password_code, reset_password, \
send_verify_email_code, verify_email, update_notification_device_id

class SendResetPasswordCodeResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        input_data = request.get_json()
        response, status = send_reset_password_code(request, input_data)
        return make_response(response, status)
    
class CheckResetPasswordCodeResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        input_data = request.get_json()
        response, status = check_reset_password_code(request, input_data)
        return make_response(response, status)
    
class ResetPasswordResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        input_data = request.get_json()
        response, status = reset_password(request, input_data)
        return make_response(response, status)
    
class SendVerifyEmailCodeResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        # input_data = request.get_json()
        response, status = send_verify_email_code(request)
        return make_response(response, status)
    
class VerifyEmailResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        input_data = request.get_json()
        response, status = verify_email(request, input_data)
        return make_response(response, status)

class UpdateNoticifactionDeviceIdResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        input_data = request.get_json()
        response, status = update_notification_device_id(request, input_data)
        return make_response(response, status)