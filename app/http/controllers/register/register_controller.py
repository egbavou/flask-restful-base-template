from app.utils.common import generate_response, request_to_json
from app.utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_500_INTERNAL_SERVER_ERROR
from db import db_session_slave, db_session_master
from app.http.requests.register.register_request import UsernameSchema, EmailSchema, RegisterSchema
from app.models.users.user_model import User
from flask_jwt_extended import create_access_token
import datetime
from sqlalchemy import or_

def check_username(request, input_data):
    """
    It check if username it's available for register
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """
    
    validator = UsernameSchema()
    errors = validator.validate(input_data)
    if errors:
        
        return generate_response(message=errors)
    
    get_user = db_session_slave.query(User.id).filter(User.username==input_data.get('username')).first()
    # get_user = username_redis_client.get('prod_api_database_username_'+str(input_data.get('username')))
    db_session_slave.commit()
    
    if get_user is None :
        
        message="Username is available"
        
        return generate_response(data=input_data,message=message, status=HTTP_200_OK)
    else:
        
        message='Username is already use'
        
        return generate_response(data=input_data,message=message,status=HTTP_200_OK)
    
def check_email(request, input_data):
    """
    It check if email it's available for register
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """

    validator = EmailSchema()
    errors = validator.validate(input_data)
    if errors:
        
        
        return generate_response(message=errors)

    get_user = db_session_slave.query(User.id).filter(User.email==input_data.get('email')).first()
    # get_user = mail_redis_client.get('prod_api_database_email_'+str(input_data.get('email')))
    db_session_slave.commit()
    
    if get_user is None:
        return generate_response(data=input_data,message='Email is available', status=HTTP_200_OK)
    else:
        return generate_response(data=input_data,message='Email is already use',status=HTTP_200_OK)
     
def register(request, input_data):
    """
    It use for register a new user
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """
    
        
    create_validation_schema = RegisterSchema()
    errors = create_validation_schema.validate(input_data)
    
    if errors:
            
        return generate_response(message=errors)

    check_user = db_session_master.query(User.id).filter(
        or_(
            User.username==input_data.get('username'),
            User.email==input_data.get('email')
        )
    ).first()

    if check_user is None:
        new_user = User(**input_data)  
        db_session_master.add(new_user)
        db_session_master.commit()
        
        token = create_access_token(str(new_user.id),expires_delta=datetime.timedelta(days=365))
        
        user = new_user.to_json()
        
        data = {
            'token' : token,
            'user': user,
        }
                
        return generate_response(
            data=data, message="User Created", status=HTTP_201_CREATED
        )
        
    else:

        db_session_master.commit()
        return generate_response(message="Username or email already exists", status=HTTP_400_BAD_REQUEST)