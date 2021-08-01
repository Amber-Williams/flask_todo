from datetime import datetime

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic') # Note 1: model starts with cap letter in db.relationship
    # Note 3: ^ For a one-to-many relationship, a db.relationship field is normally defined on the "one" side, and is used as a convenient way to get access to the "many". 
    # Note 4: backref will add a post.author expression that will return the user given a post.

    # Note 2: The __repr__ method tells Python how to print objects of this class
    def __repr__(self):
        return f'<User - id: {self.id}, Username: {self.username}, email: {self.email}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Note 1: model should be snake case when used in db.Foreignkey

    def __repr__(self):
        return f'<Post - id: {self.id}, user_id: {self.user_id}, body: {self.body} >'