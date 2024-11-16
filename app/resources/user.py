from flask_restful import Resource, reqparse
from flask import jsonify
from app.models import User
from app.schemas import UserSchema
from app.models import db

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user), 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 204

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password_hash', required=True)
        parser.add_argument('role', default='User')
        parser.add_argument('is_active', type=bool, default=True)
        data = parser.parse_args()

        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
