from app import app, db
from app.models import User, Post
from app.queries import UserQuery, PostQuery

# For the `flask shell` which helps bundle up your local shell for development
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'add_user': UserQuery.add,
        'get_user': UserQuery.get_one,
        'get_users': UserQuery.get_all,
        'add_post': PostQuery.add,
        'get_post': PostQuery.get_one,
        'get_posts': PostQuery.get_all,
        'get_user_posts': PostQuery.get_user_posts
        }