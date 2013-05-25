from joefriedl import db


class Mark(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    gravatar_id = db.Column(db.String(32))
    name = db.Column(db.String(255))
    login = db.Column(db.String(255))
    x = db.Column(db.Float)
    y = db.Column(db.Float)
