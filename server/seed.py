from app import db, create_app  # Import your app factory
from app.models import User, Category, Content, Comment, Subscription, Wishlist

def seed_data():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create Users
    user1 = User(name='Alice', email='alice@example.com', role='Admin', is_active=True)
    user2 = User(name='Bob', email='bob@example.com', role='TechWriter', is_active=True)
    user3 = User(name='Charlie', email='charlie@example.com', role='User  ', is_active=True)

    # Add users to the session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Create Categories
    category1 = Category(name='Technology')
    category2 = Category(name='Health')
    category3 = Category(name='Education')

    # Add categories to the session
    db.session.add(category1)
    db.session.add(category2)
    db.session.add(category3)

    # Create Contents
    content1 = Content(title='Latest Tech Trends', type='Article', category=category1, author=user1, is_approved=True)
    content2 = Content(title='Healthy Living Tips', type='Video', category=category2, author=user2, is_approved=True)
    content3 = Content(title='Learning Python', type='Audio', category=category3, author=user3, is_approved=False)

    # Add contents to the session
    db.session.add(content1)
    db.session.add(content2)
    db.session.add(content3)

    # Create Comments
    comment1 = Comment(content=content1, user=user2, comment_text='Great article on tech trends!')
    comment2 = Comment(content=content2, user=user3, comment_text='Very helpful tips, thanks!')

    # Add comments to the session
    db.session.add(comment1)
    db.session.add(comment2)

    # Create Subscriptions
    subscription1 = Subscription(user=user1, content=content1)
    subscription2 = Subscription(user=user2, content=content2)

    # Add subscriptions to the session
    db.session.add(subscription1)
    db.session.add(subscription2)

    # Create Wishlists
    wishlist1 = Wishlist(user=user3, content=content1)
    wishlist2 = Wishlist(user=user1, content=content2)

    # Add wishlists to the session
    db.session.add(wishlist1)
    db.session.add(wishlist2)

    # Commit the session to save all the data
    db.session.commit()

if __name__ == '__main__':
    app = create_app()  # Create your Flask app
    with app.app_context():  # Create an application context
        seed_data()  # Call the seed function