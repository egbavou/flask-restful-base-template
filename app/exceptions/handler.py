from flask import make_response
from app.utils.http_code import HTTP_404_NOT_FOUND,HTTP_500_INTERNAL_SERVER_ERROR
from flask import jsonify


def handle_404_error(error):
    """ Return 404 error in json for api"""
    
    return make_response(
        jsonify({
            'message': {
                'error' :'Not found'
            }
        }),
        HTTP_404_NOT_FOUND
    )
    
def handle_500_error(error):
    """ Return 500 error in json for api"""
    
    return make_response(
        jsonify({
            'message': {
                'error' :'Internal Server Error'
            }
        }),
        HTTP_500_INTERNAL_SERVER_ERROR
    )