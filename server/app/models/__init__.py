from app import db

from .user import User
from .content import Content
from .category import Category
from .comment import Comment
from .wishlist import Wishlist
from .subscription import Subscription

# Optionally, you can create a list of all models for easier access
__all__ = [
    'User ',
    'Content',
    'Category',
    'Comment',
    'Wishlist',
    'Subscription'
]