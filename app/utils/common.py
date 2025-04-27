from app.utils.http_code import HTTP_200_OK, HTTP_201_CREATED

def generate_response(data=None, message=None, status=400):
    """
    It takes in a data, message, and status, and returns a dictionary with the data, message, and status
    
    :param data: The data that you want to send back to the client
    :param message: This is the message that you want to display to the user
    :param status: The HTTP status code, defaults to 400 (optional)
    :return: A dictionary with the keys: data, message, status.
    """
    if status == HTTP_200_OK or status == HTTP_201_CREATED:
        status_bool = True
    else:
        status_bool = False
   
    return {
        "data": data,
        "message": modify_slz_error(message,status_bool),
        "success": status_bool,
    }, status

def modify_slz_error(message, status):
    """
    It takes a message and a status, and returns a list of errors
    
    :param message: The error message that you want to display
    :param status: The HTTP status code you want to return
    :return: A list of dictionaries.
    """
    final_error = list()
    if message:
        if type(message) == str:
            if not status:
                final_error.append({"error": message})
            else:
                final_error = message
        elif type(message) == list:
            final_error = message
        elif type(message) == dict:
            keys= list(message.keys())
            for key in keys:
                final_error.append({"error": str(key) + ": " + str(message.get(key))})
        else:
            for key, value in message.items():
                final_error.append({"error": str(key) + ": " + str(value[0])})
    else:
        final_error = None
    return final_error

def request_to_json(request, status, input_data=None, message=None, response_data={}):
    
    data = {
        'method': request.method,
        'api': request.path,
        'headers' : {
            'user_Agent': request.headers.get('User-Agent'),
            'accept': request.headers.get('Accpet'),
            'host' :  request.headers.get('Host'),
            'accept_encoding': request.headers.get('Accept-Encoding'),
            'connection': request.headers.get('Connection')
        },
        'remote_addr': request.remote_addr,
        'environ' : {
            '_charset': request._charset,
            'wsgi_version': str(request.environ.get('wsgi.version')),
            'wsgi_url_scheme': str(request.environ.get('wsgi.url_scheme')),
            'wsgi_multithread': str(request.environ.get('wsgi.multithread')),
            'wsgi_multiprocess': str(request.environ.get('wsgi.multiprocess')),
            'wsgi_run_once': str(request.environ.get('wsgi.run_once')),
            'werkzeug_socket':str(request.environ.get('werkzeug.socket')),
            'SERVER_SOFTWARE': request.environ.get('SERVER_SOFTWARE'),
            'REQUEST_METHOD': request.environ.get('REQUEST_METHOD'),
            'SCRIPT_NAME': request.environ.get('SCRIPT_NAME'),
            'PATH_INFO': request.environ.get('PATH_INFO'),
            'QUERY_STRING': request.environ.get('QUERY_STRING'),
            'REQUEST_URI': request.environ.get('REQUEST_URI'),
            'RAW_URI': request.environ.get('RAW_URI'),
            'REMOTE_ADDR': request.environ.get('REMOTE_ADDR'),
            'REMOTE_PORT': request.environ.get('REMOTE_PORT'),
            'SERVER_NAME': request.environ.get('SERVER_NAME'),
            'SERVER_PORT': request.environ.get('SERVER_PORT'),
            'SERVER_PROTOCOL': request.environ.get('SERVER_PROTOCOL'),
            'HTTP_USER_AGENT': request.environ.get('HTTP_USER_AGENT'),
            'HTTP_ACCEPT': request.environ.get('HTTP_ACCEPT'),
            'HTTP_POSTMAN_TOKEN': request.environ.get('HTTP_POSTMAN_TOKEN'),
            'HTTP_HOST': request.environ.get('HTTP_HOST'),
            'HTTP_ACCEPT_ENCODING': request.environ.get('HTTP_ACCEPT_ENCODING'),
            'HTTP_CONNECTION': request.environ.get('HTTP_CONNECTION')
        },
        'response': {
            'http_status' : status,
            'message': message,
            'data': response_data
        },
        'params' : input_data,
        'http_status' : status,

    }
    
    return data