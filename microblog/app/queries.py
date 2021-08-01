from app import app, db
from app.models import User, Post

class UserQuery():
    def get_all():
        return User.query.all()
    
    def get_one(id):
        return User.query.get(id)
    
    def add(username, email):
        u = User(username, email)
        db.session.add(u)
        db.session.commit()

class PostQuery():
    def get_all():
        return Post.query.all()
    
    def get_one(id):
        return Post.query.get(id)
    
    def add(body, author_id):
        # author must be type of user!
        u = User.query.get(author_id)
        p = Post(body=body, author=u)
        db.session.add(p)
        db.session.commit()

    def get_user_posts(user_id):
        user = get_user(user_id)
        return user.posts.all()
