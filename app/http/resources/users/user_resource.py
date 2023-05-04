from flask import Response
from flask_restful import Resource
from flask import request, make_response
from app.http.controllers.users.user_controller import create_user,user_list,delete_user,edit_user


class UserResource(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = create_user(request, input_data)
        return make_response(response, status)
    
    @staticmethod
    def get() -> Response:
        """GET ALL USERS IN DATABASE"""
        response, status = user_list()
        return make_response(response, status)
    
    # def get(self, todo_id=None):
    #     if todo_id:
    #         todo = Todo.query.filter_by(id=todo_id).first()
    #         return marshal(todo, todo_fields)
    #     else:
    #         args = request.args.to_dict()
    #         limit = args.get('limit', 0)
    #         offset = args.get('offset', 0)

    #         args.pop('limit', None)
    #         args.pop('offset', None)

    #         todo = Todo.query.filter_by(**args).order_by(Todo.id)
    #         if limit:
    #             todo = todo.limit(limit)

    #         if offset:
    #             todo = todo.offset(offset)

    #         todo = todo.all()

    #         return marshal({
    #             'count': len(todo),
    #             'todos': [marshal(t, todo_fields) for t in todo]
    #         }, todo_list_fields)

    
    def put(self, user_id=None):
       
        input_data = request.get_json()
        response, status = edit_user(request, input_data,user_id)
        return make_response(response, status)

    def delete(self, user_id=None):
        
        response, status = delete_user(user_id)
        return make_response(response, status)

class UserListApi(Resource): 
    @staticmethod
    def get() -> Response:
        """GET ALL USERS IN DATABASE"""
        response, status = user_list()
        return make_response(response, status)