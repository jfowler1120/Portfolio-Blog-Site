from datetime import datetime
from blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(40), nullable=False, default ='default.jpg')
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hearts = db.relationship('PostHeart', backref='post', lazy='dynamic')
    comments = db.relationship('PostComment', backref='article', lazy=True)
    
    def get_comments(self):
        return PostComment.query.filter_by(post_id=post.id).order_by(PostComment.date.desc())

    def __repr__(self):
        return f"Post('{self.date}', '{self.title}', '{self.content}')"

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128))
    email = db.Column(db.String(120), nullable=False)
    post = db.relationship('Post', backref='user', lazy=True)
    hearted = db.relationship('PostHeart', foreign_keys='PostHeart.user_id', backref='user', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def heart_post(self, post):
        if not self.has_hearted_post(post):
            heart = PostHeart(user_id=self.id,post_id=post.id)
            db.session.add(heart)

    def unheart_post(self, post):
        if self.has_hearted_post(post):
            PostHeart.query.filter_by(
                user_id=self.id,
                post_id=post.id).delete()
            
    def has_hearted_post(self, post):
        return PostHeart.query.filter(
            PostHeart.user_id == self.id,
            PostHeart.post_id == post.id).count() > 0

    @property
    def password(self):
        raise AttributeError('Password is not readable.')

    @password.setter
    def password(self,password):
        self.hashed_password=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class PostHeart(db.Model):
    __tablename__ = 'post_heart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

#(modified from https://stackoverflow.com/questions/52665707/how-do-i-implement-a-like-button-function-to-posts-in-python-flask)

class PostComment(db.Model):
    __tablename__ = 'post_comments'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.Column(db.String(20), db.ForeignKey('user.username'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Comment('{self.text}', '{self.date}')"

#(modified from https://stackoverflow.com/questions/71909035/how-to-delete-a-comment-and-return-to-the-post-id-page-in-flask)