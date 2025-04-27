from flask import Response
from flask_restful import Resource
from flask import request, make_response
from app.http.controllers.sms.sms_controller import send_sms

class SendSMSResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = send_sms(request, input_data)
        return make_response(response, status)