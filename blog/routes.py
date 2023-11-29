from flask import Flask, render_template, url_for, request, redirect, flash
from blog import app, db
import timeago, datetime
from blog.models import User, Post, PostHeart, PostComment
from blog.forms import RegistrationForm, LoginForm, AddCommentForm
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')

@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About Me')

@app.route("/myskills")
def myskills():
    return render_template('myskills.html', title='My Skills')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = AddCommentForm()
    return render_template('post.html', title=post.title, post=post, form=form)

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('registered'))
    return render_template('register.html',title='Register',form=form)

@app.route("/registered")
def registered():
    return render_template('registered.html', title='Thanks!')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('You\'ve successfully logged in,'+' '+ current_user.username +'!')
            return redirect(url_for('home'))
        flash('Invalid username or password.')
    return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('Logout successful!')
    return redirect(url_for('home'))

@app.route('/heart/<int:post_id>/<action>')
@login_required
def heart_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'heart':
        current_user.heart_post(post)
        db.session.commit()
    if action == 'unheart':
        current_user.unheart_post(post)
        db.session.commit()
    return redirect(request.referrer)

@app.route("/post/<int:post_id>/postcomment", methods=["GET", "POST"])
@login_required
def comment_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = AddCommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            comment = PostComment(text=form.text.data, post_id=post.id, author_id=current_user.id, author=current_user.username)
            db.session.add(comment)
            db.session.commit()
            flash("You commented on the post!")
            return redirect(url_for("post", post_id=post.id))
    return render_template("post.html", title = "Post", form=form, post_id=post.id)

@app.route("/deletecomment/<int:id>", methods=["GET", "POST"])
@login_required
def deletecomment(id):
    comment_to_delete = PostComment.query.get_or_404(id)
    try:
        db.session.delete(comment_to_delete)
        db.session.commit()
        flash("Comment deleted.")
        return redirect(request.referrer)
    except:
        flash("There was a problem deleting the comment.")
        return redirect(request.referrer)

@app.template_filter('timeago')
def fromnow(date):
    return timeago.format(date, datetime.datetime.now())