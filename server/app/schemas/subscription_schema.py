from marshmallow import Schema, fields, validate
from app.models.subscription import Subscription

class SubscriptionSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    content_id = fields.Int(required=True, validate=validate.Range(min=1))
    created_at = fields.DateTime(dump_only=True)

    class Meta:
        fields = ('id', 'user_id', 'content_id', 'created_at')