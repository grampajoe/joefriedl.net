from flask import Flask


__all__ = ['app']


app = Flask(__name__)
app.config.from_object('config')


import views
