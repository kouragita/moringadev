from app import db

class Wishlist(db.Model):
    __tablename__ = 'wishlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    # Relationships
    owner = db.relationship('User ', back_populates='wishlists', lazy=True)  # Changed to back_populates
    category = db.relationship('Category', back_populates='wishlists', lazy=True)