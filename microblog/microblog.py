from app import app, db
from app.models import User, Post

# custom helper functions that help me use the shell to interact with the db
def get_users():
    return User.query.all()

def get_user(id):
    return User.query.get(id)

def add_user(username, email):
     u = User(username='susan', email='susan@example.com')
     db.session.add(u)
     db.session.commit()

def get_posts():
    return Post.query.all()

def get_post(id):
    return Post.query.get(id)
    
def add_post(body, author_id)
    # author must be type of user!
    u = User.query.get(author_id)
    p = Post(body=body, author=u)
    db.session.add(p)
    db.session.commit()

# For the `flask shell` which helps bundle up your local shell for development
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Users': get_users(), 'Posts': get_users()}