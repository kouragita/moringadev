from marshmallow import Schema, fields
from app.models.user import User

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    role = fields.Str(required=True)
    is_active = fields.Bool(default=True)