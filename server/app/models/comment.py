from app import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment_text = db.Column(db.String(), nullable=False)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)

    # Relationships
    content = db.relationship('Content', back_populates='comments', lazy=True)  # Changed to back_populates
    user = db.relationship('User ', back_populates='comments', lazy=True)  # Removed extra space and changed to back_populates
    parent_comment = db.relationship('Comment', remote_side=[id], back_populates='replies', lazy=True)  # Changed to back_populates
    replies = db.relationship('Comment', back_populates='parent_comment', lazy=True)  # Added replies relationship