from marshmallow import Schema, fields
from app.models.category import Category

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()