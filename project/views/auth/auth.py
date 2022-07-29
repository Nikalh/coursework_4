from flask_restx import Namespace, Resource
from flask import request

from project.container import user_service

from project.setup.api.models import user

api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.create_user(data.get('email'), data.get('password')), 201
        else:
            return 'Что-то не передано', 401


@api.route('/login/')
class LoginView(Resource):
    @api.response(404, 'Not found')
    def post(self):
        req_json = request.json

        if req_json.get('email') and req_json.get('password'):
            return user_service.check(req_json.get('email'), req_json.get('password'))
        else:
            return 'Чего-то не хватает', 401

    @api.response(404, 'Not found')
    def put(self):
        req_json = request.json
        if req_json.get('refresh_token') and req_json.get('access_token'):
            return user_service.update_token('refresh_token'), 201
        else:
            return 'Что-то не передано', 401
