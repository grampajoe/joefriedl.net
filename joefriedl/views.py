import os
import requests
import logging

from flask import render_template, url_for, session, request, redirect

from joefriedl import app, db
from joefriedl.models import Mark


# Set up some basic logging for now
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


@app.route('/')
def index():
    marks = Mark.query.all()
    if 'user' in session:
        user_mark = Mark.query.get((session['user']['id']))
    else:
        user_mark = None
    return render_template(
        'index.html', marks=marks, client_id=app.config['GH_CLIENT_ID'],
        user_mark=user_mark)


@app.route('/marks/', methods=['POST'])
def marks():
    if request.method == 'POST':
        store_mark(request.form['x'], request.form['y'], session['user'])

        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    """Log a user out."""
    if 'user' in session:
        del session['user']

    return redirect(url_for('index'))


@app.route('/auth/github')
def auth_github():
    code = request.args.get('code', None)

    if code is not None:
        access_token = get_github_access_token(code)
        session['user'] = get_github_user_info(access_token)

    return redirect(url_for('index'))


def store_mark(x, y, user):
    """Store the location of a mark, along with the user."""
    mark = Mark.query.get((user['id']))

    if mark is None:
        mark = Mark(user_id=user['id'])

    mark.gravatar_id = user['gravatar_id']
    mark.name = user['name']
    mark.login = user['login']
    mark.x = x
    mark.y = y

    db.session.add(mark)
    db.session.commit()

    logger.info(
        '{name} made a mark at {x}, {y}'.format(name=user['name'], x=x, y=y)
    )


def get_github_access_token(code):
    """Get an access token from GitHub."""
    response = requests.post(
        'https://github.com/login/oauth/access_token',
        data={
            'client_id': app.config['GH_CLIENT_ID'],
            'client_secret': app.config['GH_CLIENT_SECRET'],
            'code': code,
        },
        headers={
            'Accept': 'application/json',
        },
    )

    data = response.json()
    return data['access_token']


def get_github_user_info(access_token):
    """Get information about the logged in GitHub user."""
    response = requests.get(
        'https://api.github.com/user',
        params={
            'access_token': access_token,
        },
        headers={
            'Accept': 'application/json',
        },
    )

    data = response.json()
    return data
