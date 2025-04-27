
from flask import Response
from flask_restful import Resource
from flask import make_response

class HomeResource(Resource):
    @staticmethod
    def get() -> Response:
        return make_response({},200)