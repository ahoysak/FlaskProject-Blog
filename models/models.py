from app import db, app, manager
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    user_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email_user = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    articles = db.relationship('Article', backref='users', passive_deletes=True)
    comments = db.relationship('Comment', backref='users', passive_deletes=True)
    likes = db.relationship('Like', backref='users', passive_deletes=True)


class Article(db.Model):
    name_article = db.Column(db.String(80),  nullable=False)
    text_article = db.Column(db.Text,  nullable=False)
    category = db.Column(db.String(100),  nullable=False)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"),  nullable=False)
    comments = db.relationship('Comment', backref='article', passive_deletes=True)
    likes = db.relationship('Like', backref='article', passive_deletes=True)
    like_count = db.Column(db.Integer, default=0, nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    text_comment = db.Column(db.String(250), nullable=False )
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"),  nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('article.id', ondelete="CASCADE"),  nullable=False)


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'article.id', ondelete="CASCADE"), nullable=False)


@manager.user_loader
def load_user(id_user):
    return Users.query.get(id_user)
