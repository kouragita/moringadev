from flask import Blueprint

# Create a main blueprint
main = Blueprint('main', __name__)

# Import routes
from .user_routes import *
from .content_routes import *
from .category_routes import *
from .comment_routes import *
from .wishlist_routes import *
from .subscription_routes import *

# Register the routes with the main blueprint
def register_routes(app):
    app.register_blueprint(main)