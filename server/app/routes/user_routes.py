from flask import request, jsonify, abort
from app.models import db
from app.models.user import User
from app.schemas.user_schema import UserSchema
from . import main

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@main.route('/users', methods=['POST'])
def create_user():
    json_data = request.get_json()
    user_data = user_schema.load(json_data)
    user = User(**user_data)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), 201

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.dump(users), 200

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    return user_schema.dump(user), 200

@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)

    json_data = request.get_json()
    user_data = user_schema.load(json_data)
    for key, value in user_data.items():
        setattr(user, key, value)
    db.session.commit()
    return user_schema.dump(user), 200

@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)

    db.session.delete(user)
    db.session.commit()
    return '', 204