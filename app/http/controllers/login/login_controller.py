from app.models.users.user_model import User
from app.utils.common import generate_response, request_to_json
from app.http.requests.login.login_request import LoginSchema,LogoutSchema
from app.utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_202_ACCEPTED, HTTP_500_INTERNAL_SERVER_ERROR
from flask_jwt_extended import create_access_token
import datetime
from db import db_session_slave
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required,get_jwt, get_jwt_identity
from redis_client import jwt_redis_blocklist
from flask_bcrypt import check_password_hash

ACCESS_EXPIRES = datetime.timedelta(days=365)
 
@jwt_required()
def auth_user(request):

    data = current_user.to_json()

    return generate_response(
        data=data, status=HTTP_200_OK
    )
    
def login(request, input_data):
    """
    It's use for login
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """      

    validator = LoginSchema()
    errors = validator.validate(input_data)
    if errors:
        
        return generate_response(message=errors)
    
    if input_data.get('type') == 'username': 
        get_user = db_session_slave.query(User).filter(User.username==input_data.get('username')).first()
    elif input_data.get('type') == 'email': 
        get_user = db_session_slave.query(User).filter(User.email==input_data.get('email')).first()

    db_session_slave.commit()
        
    if get_user is None:
        
        message = "User not found"
        
        return generate_response(message=message, status=HTTP_400_BAD_REQUEST)
    
    if get_user.deleted_at is not None:
        
        message = "User delete his account"

        return generate_response(message=message, status=HTTP_401_UNAUTHORIZED)

    if get_user.is_suspended:
        
        message = "User is suspended"

        return generate_response(message=message, status=HTTP_401_UNAUTHORIZED)
        
    if check_password_hash(get_user.password,input_data.get("password")):        
            
        token = create_access_token(str(get_user.id),expires_delta=datetime.timedelta(days=365))
        
        data = {
            'token' : token,
            'user': get_user.to_json(),
        }
        
        
        return generate_response(
            data=data, message="User login successfully", status=HTTP_200_OK
        )
            
    else:
        message = "Password is wrong"
        
        return generate_response(
            message=message, status=HTTP_400_BAD_REQUEST
        )
    
    

@jwt_required()
def logout(request,input_data):
    """
    It's use for logout a user
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """

    validator = LogoutSchema()
    errors = validator.validate(input_data)
    if errors:
        
        return generate_response(message=errors)
    
    token = get_jwt()
    jti = token["jti"]
    ttype = token["type"]
    jwt_redis_blocklist.set(jti, "", ex=ACCESS_EXPIRES)
    
    message = f"{ttype.capitalize()} token successfully revoked"
    
    return generate_response(
        data={}, message=message, status=HTTP_200_OK
    )
    

@jwt_required()
def refresh(request):
    """
    It's use for refresh authentificate user token
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """        

    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    
    return generate_response(
        data={
            'token':access_token
        }, 
        message="",
        status=HTTP_200_OK
    )