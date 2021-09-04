from datetime import datetime

from app import app, db, login
from app.models import User, Post

class UserQuery():
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def get_all():
        return User.query.all()
    
    def get_one(username=None, email=None):
        if username is None and email:
            return User.query.filter_by(email=email).first()
        return User.query.filter_by(username=username).first()
    
    def add(username, email, password):
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
    
    def update_last_seen(user):
        user.last_seen = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
    
    def update_about_me(user, username, about_me):
        user.username = username
        user.about_me = about_me
        db.session.add(user)
        db.session.commit()

class PostQuery():
    def get_all():
        return Post.query.all()
    
    def get_one(id):
        return Post.query.get(id)
    
    def add(body, author_name):
        user = UserQuery.get_one(author_name)
        post = Post(body=body, author=user)
        db.session.add(post)
        db.session.commit()

    def get_author_posts(author_name):
        user = UserQuery.get_one(author_name)
        return user.posts.all()
