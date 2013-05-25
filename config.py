import os


DEBUG = os.environ.get('DEBUG', False)

SECRET_KEY = os.environ['SECRET_KEY']

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

GH_CLIENT_ID = os.environ['GH_CLIENT_ID']
GH_CLIENT_SECRET = os.environ['GH_CLIENT_SECRET']
