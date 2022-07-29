import jwt
from flask import request, current_app

from project.services import users_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get('AUTH_AUTORIZATION', "").replace('Bearer', '')

        if not token:
            return "Вы не передали токен в заголовке"
        try:
            jwt.decode(token,
                       key=current_app.config['SECRET_KEY'],
                       algorithms=current_app.config['ALGORITHM'])
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return e

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get('AUTH_AUTORIZATION', '').replace('Bearer', '')

        if not token:
            return "Вы не передали токен в заголовке"
        try:
            data = jwt.decode(token,
                              key=current_app.config['SECRET_KEY'],
                              algorithms=current_app.config['ALGORITHM'])

            user = users_service.get_by_email(data.get('email'))
            if user:
                if not user.email == 'email':
                    return 'Вам доступ запрещен'
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return "Ошибка валидации токена"

    return wrapper
