import os
import requests

from flask import render_template, url_for, session, request, redirect

from joefriedl import app


@app.route('/')
def index():
    return render_template('index.html', client_id=app.config['GH_CLIENT_ID'])


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
    print user['name'], 'made a mark at', x, ',', y


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
