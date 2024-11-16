from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate

# Extensions
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringadaily.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api = Api(app)
    CORS(app)

    # Import routes after app creation
    from app.resources import user, content, category, comment, wishlist, subscription  # Use absolute imports

    # User routes
    api.add_resource(user.UserListResource, '/users')
    api.add_resource(user.UserResource, '/users/<int:user_id>')

    # Content routes
    api.add_resource(content.ContentListResource, '/contents')
    api.add_resource(content.ContentResource, '/contents/<int:content_id>')

    # Category routes
    api.add_resource(category.CategoryListResource, '/categories')
    api.add_resource(category.CategoryResource, '/categories/<int:category_id>')

    # Comment routes
    api.add_resource(comment.CommentListResource, '/comments')
    api.add_resource(comment.CommentResource, '/comments/<int:comment_id>')

    # Wishlist routes
    api.add_resource(wishlist.WishlistListResource, '/wishlists')
    api.add_resource(wishlist.WishlistResource, '/wishlists/<int:wishlist_id>')

    # Subscription routes
    api.add_resource(subscription.SubscriptionListResource, '/subscriptions')
    api.add_resource(subscription.SubscriptionResource, '/subscriptions/<int:user_id>/<int:category_id>')

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
