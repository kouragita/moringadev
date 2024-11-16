from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    
    # Load configuration from config.py or another configuration file
    app.config.from_object(config_class)
    
    # Initialize extensions with the app
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Import models here to register them with SQLAlchemy
    with app.app_context():
        from .models import (
            User, Content, Category, Comment, Wishlist, Subscription
        )
        db.create_all()  # Create tables for all models
    
    # Import and register your blueprints or APIs here
    from .routes import main as main_routes
    app.register_blueprint(main_routes)  # Register main API routes

    return app