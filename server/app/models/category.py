from app import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    # Relationships
    contents = db.relationship('Content', back_populates='category', lazy=True)
    subscriptions = db.relationship('Subscription', back_populates='category', lazy=True)
    wishlists = db.relationship('Wishlist', back_populates='category', lazy=True)