import json
# import jwt
# import datetime
# from api import db
from app.models.users.user_model import User
from app.utils.common import generate_response
from app.http.requests.users.user_request import CreateUserInputSchema, EditUserInputSchema
from db import db
from app.utils.http_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

def create_user(request, input_data):
    """
    It creates a new user
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """
    create_validation_schema = CreateUserInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    check_username_exist = User.query.filter_by(
        username=input_data.get("username")
    ).first()
    
    check_email_exist = User.query.filter_by(email=input_data.get("email")).first()
    
    check_phone_number_exist = User.query.filter_by(phone_number=input_data.get("phone_number")).first()
    
    if check_username_exist:
        return generate_response(
            message="Username already exist", status=HTTP_400_BAD_REQUEST
        )
    elif check_email_exist:
        return generate_response(
            message="Email  already taken", status=HTTP_400_BAD_REQUEST
        )
    elif check_phone_number_exist:
        return generate_response(
            message="Phone number  already taken", status=HTTP_400_BAD_REQUEST
        )

    new_user = User(**input_data)  # Create an instance of the User class
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Comment
    
    return generate_response(
        data=input_data, message="User Created", status=HTTP_201_CREATED
    )
    
def user_list(user_id=None): 
    
    if user_id: 
        data = User.query.filter_by(id=user_id).first()
        data = data.json()
    else:
        data = User.query.all()
        data =  [user.json() for user in User.query.all()]
    
    return generate_response(
        data=data, status=HTTP_200_OK
    )

def delete_user(user_id):
    
    user = User.query.get(user_id)
    
    if user is None:
        return generate_response(
            message="User not found", status=HTTP_404_NOT_FOUND
        )
        
    db.session.delete(user)
    db.session.commit()
    
    return generate_response(
        data=user.json(), status=HTTP_200_OK
    )
        
def edit_user(request, input_data,user_id):
    
    """
    It creates a new user
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """
    
    user = User.query.get(user_id)
    
    if user is None:
        return generate_response(
            message="User not found", status=HTTP_404_NOT_FOUND
        )
        
    edit_validation_schema = EditUserInputSchema()
    errors = edit_validation_schema.validate(input_data)
    
    if errors:
        return generate_response(message=errors)
    
    check_username_exist = User.query.filter_by(
        username=input_data.get("username"),
    ).first()
    
    check_email_exist = User.query.filter_by(
        email=input_data.get("email"),
    ).first()
    
    check_phone_number_exist = User.query.filter_by(
        phone_number=input_data.get("phone_number"),
    ).first()
    
    if check_username_exist and check_username_exist.id != user.id:
        return generate_response(
            message="Username already exist", status=HTTP_400_BAD_REQUEST
        )
    elif check_email_exist and check_username_exist.id != user.id:
        return generate_response(
            message="Email  already taken", status=HTTP_400_BAD_REQUEST
        )
    elif check_phone_number_exist and check_username_exist.id != user.id:
        return generate_response(
            message="Phone number  already taken", status=HTTP_400_BAD_REQUEST
        )
        
    if input_data.get('age'):
        user.age = input_data.get('age')
        
    if input_data.get('phone_number'):
        user.phone_number = input_data.get('phone_number')
        
    if input_data.get('username'):
        user.username = input_data.get('username')
        
    if input_data.get('last_name'):
        user.last_name = input_data.get('last_name')
        
    if input_data.get('first_name'):
        user.first_name = input_data.get('first_name')

    db.session.commit()
    
    return generate_response(
        data=input_data, message="User Edited", status=HTTP_201_CREATED
    )