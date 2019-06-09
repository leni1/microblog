from flask import flash, redirect, render_template, url_for

from blog import app
from blog.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Leni'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Kampala!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Matrix is a really cool movie!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
