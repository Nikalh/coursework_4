from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Гайдай'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Спорт лото 82'),
    'description': fields.String(required=True, max_length=100, example='Жизненая комедия'),
    'trailer': fields.String(required=True, max_length=100, example='Спорт лото 82'),
    'year': fields.Integer(required=True, example=1982),
    'rating': fields.Float(),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Иван'),
    'surname': fields.String(required=True, max_length=100, example='Иванов'),
    'password': fields.String(required=True, max_length=100, example='Комедия'),
    'email': fields.String(required=True, max_length=100, example='sdsad@ya.ru'),
    'favorite_genre': fields.String(required=True, max_length=100, example='Комедия'),
})
