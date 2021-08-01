from flask import render_template, request, session, flash, url_for, redirect

from app import app
from app.forms import LoginForm

def generate_index_content(username):
    username = {'username': username}
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

    return { "username": username, "posts": posts}

@app.route('/')
@app.route('/index')
def index_page():
    # check if contenet in session else user needs to login first
    if 'username' in session:
        content = generate_index_content(session['username'])
    else:
        return redirect(url_for('login_page'))

    return render_template('index.html', title='Home', user=content['username'], posts=content['posts'])

@app.route('/login', methods=['GET'])
def login_page():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()

    username = form.username.data
    remember_me = form.remember_me.data # true / false

    print('form.username.data', form.username.data)

    flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')

    # take form data and put needed parts into session
    session['username'] = username
    
    return redirect(url_for('index_page'))