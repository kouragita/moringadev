from app import db

class Subscription(db.Model):
    __tablename__ = 'subscriptions'  # It's a good practice to define the table name explicitly

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Ensure 'users' matches the table name
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)  # Ensure 'contents' matches the table name
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships
    user = db.relationship('User ', back_populates='subscriptions', lazy=True)  # Changed to back_populates
    content = db.relationship('Content', back_populates='subscriptions', lazy=True)  # Changed to back_populates

    def __repr__(self):
        return f'<Subscription {self.id} - User ID: {self.user_id} - Content ID: {self.content_id}>'