from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


__all__ = ['app', 'db']


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import views
