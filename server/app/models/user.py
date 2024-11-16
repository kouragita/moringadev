from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.Enum('Admin', 'TechWriter', 'User '), nullable=False)  # Ensure no extra space
    is_active = db.Column(db.Boolean, default=True)

    # Relationships
    contents = db.relationship('Content', back_populates='author', lazy=True)  # Changed to back_populates
    comments = db.relationship('Comment', back_populates='user', lazy=True)  # Changed to back_populates
    wishlists = db.relationship('Wishlist', back_populates='owner', lazy=True)
    subscriptions = db.relationship('Subscription', back_populates='user', lazy=True)