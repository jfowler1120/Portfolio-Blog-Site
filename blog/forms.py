from flask_wtf import FlaskForm
import timeago, datetime
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, InputRequired, Regexp, EqualTo
from blog.models import User, Post, PostHeart, PostComment

class RegistrationForm(FlaskForm):
    username = StringField('Username:',validators=[DataRequired(),Regexp('^[a-z0-9]{8,20}$',message='Your username should be between 8 and 20 characters long, and cannot contain any symbols or capital letters.')])
    email = EmailField('Email Address:',validators=[DataRequired()])
    password = PasswordField('Password:',validators=[DataRequired(),Regexp('^.{8,32}$',message='Your password must be between 8 and 32 characters long.'),EqualTo('confirm_password', message='Passwords do not match. Try again')])
    confirm_password = PasswordField('Confirm Password:',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(message='Username already exists. Please choose a different one!')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_user(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError(message='User does not exist.')

class AddCommentForm(FlaskForm):
    text = StringField("Comment", validators=[InputRequired()])
    submit = SubmitField("Post")