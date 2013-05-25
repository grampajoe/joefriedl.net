from joefriedl import db


class Mark(db.Model):
    """A mark."""
    user_id = db.Column(db.Integer, primary_key=True)
    gravatar_id = db.Column(db.String(32))
    name = db.Column(db.String(255))
    login = db.Column(db.String(255))
    x = db.Column(db.Float)
    y = db.Column(db.Float)

    @property
    def gravatar_url(self):
        """Return the gravatar URL for a mark."""
        return 'https://secure.gravatar.com/avatar/%s' % self.gravatar_id

    @property
    def url(self):
        """Return the user's URL."""
        return 'https://github.com/%s' % self.login
