from sqlalchemy import Column, String
from marshmallow import Schema, fields

from project.setup.api import models
from project.setup.db import models, db


class Genre(models.Base):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class User(models.Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    favorite_genre = db.Column(db.Integer, db.ForeignKey(f'{Genre.__tablename__}.id'))
    genre = db.relationship ('Genre')


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    surname = fields.Str()
    password = fields.Str()
    email = fields.Str()
    favorite_genre = fields.Str()


class Director(models.Base):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class Movie(models.Base):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey(f'{Genre.__tablename__}.id'), nullable=False)
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey(f'{Director.__tablename__}.id'), nullable=False)
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
