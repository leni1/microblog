from flask import render_template

from blog import app


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
