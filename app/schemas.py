from marshmallow import Schema, fields, validate, EXCLUDE
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from .models import User, Content, Category, Comment, Wishlist, Subscription


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        unknown = EXCLUDE  # Ignore unknown fields during deserialization

    id = auto_field()
    name = auto_field()
    email = auto_field()
    role = auto_field()
    is_active = auto_field()
    contents = fields.List(fields.Nested(lambda: ContentSchema(exclude=("author",))))
    comments = fields.List(fields.Nested(lambda: CommentSchema(exclude=("user",))))
    wishlist = fields.List(fields.Nested(lambda: WishlistSchema(exclude=("user",))))
    subscriptions = fields.List(fields.Nested(lambda: SubscriptionSchema(exclude=("user",))))


class ContentSchema(SQLAlchemySchema):
    class Meta:
        model = Content
        load_instance = True
        unknown = EXCLUDE

    id = auto_field()
    title = auto_field()
    type = auto_field()
    is_approved = auto_field()
    category = fields.Nested("CategorySchema", exclude=("contents",))
    author = fields.Nested("UserSchema", exclude=("contents",))
    comments = fields.List(fields.Nested("CommentSchema", exclude=("content",)))
    wishlist_entries = fields.List(fields.Nested("WishlistSchema", exclude=("content",)))


class CategorySchema(SQLAlchemySchema):
    class Meta:
        model = Category
        load_instance = True
        unknown = EXCLUDE

    id = auto_field()
    name = auto_field()
    contents = fields.List(fields.Nested("ContentSchema", exclude=("category",)))
    subscriptions = fields.List(fields.Nested("SubscriptionSchema", exclude=("category",)))


class CommentSchema(SQLAlchemySchema):
    class Meta:
        model = Comment
        load_instance = True
        unknown = EXCLUDE

    id = auto_field()
    comment_text = auto_field()
    content = fields.Nested("ContentSchema", exclude=("comments",))
    user = fields.Nested("UserSchema", exclude=("comments",))
    parent = fields.Nested("CommentSchema", exclude=("replies",))
    replies = fields.List(fields.Nested("CommentSchema", exclude=("parent",)))


class WishlistSchema(SQLAlchemySchema):
    class Meta:
        model = Wishlist
        load_instance = True
        unknown = EXCLUDE

    id = auto_field()
    user = fields.Nested("UserSchema", exclude=("wishlist",))
    content = fields.Nested("ContentSchema", exclude=("wishlist_entries",))


class SubscriptionSchema(SQLAlchemySchema):
    class Meta:
        model = Subscription
        load_instance = True
        unknown = EXCLUDE

    user = fields.Nested("UserSchema", exclude=("subscriptions",))
    category = fields.Nested("CategorySchema", exclude=("subscriptions",))
