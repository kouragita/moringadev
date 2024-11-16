from app import db

class Content(db.Model):
    __tablename__ = 'contents'  # Ensure this matches the foreign key reference

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(), nullable=False)
    type = db.Column(db.Enum('Video', 'Audio', 'Article'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)

    # Relationships
    category = db.relationship('Category', back_populates='content_items', lazy=True)
    comments = db.relationship('Comment', back_populates='content', lazy=True)
    wishlists = db.relationship('Wishlist', back_populates='content', lazy=True)
    author = db.relationship('User ', back_populates='contents', lazy=True)  # Ensure no extra space