import base64
import hashlib
import calendar
import datetime


import jwt
from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')

def compare_password_hash(other_password, password_hash):
    """
    Сравнение паролей
    :param password_user: пароль пользователя
    :param password_hash: пароль в хеше
    :return:
    """
    return generate_password_hash(other_password) == password_hash


def generate_token(email, password, password_hash=None, is_refresh=True):
    if email is None:
        return None
    if not is_refresh:
        if not compare_password_hash(other_password=password, password_hash=password_hash):
            return None

    data = {
        "email": email,
        "password": password
    }

    # время действия токена 15 минут
    min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
    data['exp'] = calendar.timegm(min15.timetuple())
    access_token = jwt.encode(data, key=current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])

    # время действия токена дней
    min_day = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_DAYS'])
    data['exp'] = calendar.timegm(min_day.timetuple())
    refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def approve_refresh_token(refresh_token):
    """
    Метод получает информацию о пользователе. извлекает значение email и по
    refrech_token
    """
    data = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'], algorithms=current_app.config['ALGORITHM'])

    email = data.get('email')
    password = data.get('password')

    return generate_token(email, password, is_refresh=True)


def get_data_from_token(refresh_token):

    try:
        data = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'], algorithms=current_app.config['ALGORITHM'])
        return data
    except Exception:
        return None
