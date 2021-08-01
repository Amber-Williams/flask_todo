from flask import render_template, request, session, flash, url_for, redirect
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app
from app.forms import LoginForm, RegistrationForm
from app.queries import UserQuery

posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
]


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    # POST request
    if form.validate_on_submit():
        username = form.username.data
        remember = form.remember_me.data # true / false
        password = form.password.data

        user = UserQuery.get_one(username)

        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            session['username'] = username  # here only to show we can add stuff to a user's session
            login_user(user, remember=remember)
            # if user previously tried to access a page but was routed to login first
            # we route them back to that page
            # extra security: next is a full URL that includes a domain name, redirect to the index page
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)

    # GET request
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    # POST request
    if form.validate_on_submit():
        UserQuery.add(username=form.username.data, email=form.email.data, password=form.password.data)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    # GET request
    return render_template('register.html', title='Register', form=form)