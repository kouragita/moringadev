from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum('Admin', 'TechWriter', 'User', name='user_roles'), default='User')
    is_active = db.Column(db.Boolean, default=True)

    # Relationships
    contents = db.relationship('Content', back_populates='author', lazy=True)
    comments = db.relationship('Comment', back_populates='user', lazy=True)
    subscriptions = db.relationship('Subscription', back_populates='user', lazy=True)
    wishlist = db.relationship('Wishlist', back_populates='user', lazy=True)


class Content(db.Model):
    __tablename__ = 'contents'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    type = db.Column(db.Enum('Video', 'Audio', 'Article', name='content_types'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)

    # Relationships
    category = db.relationship('Category', back_populates='contents')
    author = db.relationship('User', back_populates='contents')
    comments = db.relationship('Comment', back_populates='content', lazy=True)
    wishlist_entries = db.relationship('Wishlist', back_populates='content', lazy=True)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    # Relationships
    contents = db.relationship('Content', back_populates='category', lazy=True)
    subscriptions = db.relationship('Subscription', back_populates='category', lazy=True)



class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)

    # Relationships
    content = db.relationship('Content', back_populates='comments')
    user = db.relationship('User ', back_populates='comments')
    
    # Self-referential relationship for replies
    replies = db.relationship('Comment', 
                               backref=db.backref('parent', remote_side=[id]), 
                               lazy='dynamic')

    def __repr__(self):
        return f'<Comment {self.id}: {self.comment_text}>'


class Wishlist(db.Model):
    __tablename__ = 'wishlists'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='wishlist')
    content = db.relationship('Content', back_populates='wishlist_entries')


class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)

    # Relationships
    user = db.relationship('User', back_populates='subscriptions')
    category = db.relationship('Category', back_populates='subscriptions')
