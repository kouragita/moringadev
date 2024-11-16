from marshmallow import Schema, fields

class WishlistSchema(Schema):
    id = fields.Int(dump_only=True)  
    user_id = fields.Int(required=True)  
    item_name = fields.Str(required=True)  
    description = fields.Str(allow_none=True)  


wishlist_schema = WishlistSchema()
wishlists_schema = WishlistSchema(many=True)  