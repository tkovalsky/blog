from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Todd'}
    posts = [
        {
            'author': {'username':'Ted'},
            'body': 'Sunny in San Fran!' ,
        },
        {
            'author': {'username':'Sally'},
            'body': 'Snow in Boston :(',
        }


    ]





    return render_template('index.html', title='Home', user=user, posts=posts)
