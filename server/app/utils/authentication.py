import jwt
from flask import current_app
from app.models import User

def generate_token(user_id):
    token = jwt.encode({'user_id': user_id}, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token

def verify_token(token):
    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return data['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None