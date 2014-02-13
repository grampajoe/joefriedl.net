"""
Those views tho
"""
from flask import render_template

from joefriedl import app


@app.route('/')
def index():
    return render_template('index.html')
