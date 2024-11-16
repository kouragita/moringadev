from marshmallow import Schema, fields
from app.models.comment import Comment

class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    user_id = fields.Int(required=True)  # Assuming a foreign key to User
    content_id = fields.Int(required=True)  # Assuming a foreign key to Content