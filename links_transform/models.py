from links_transform import db


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_postfix = db.Column(db.String(50))
    long_url = db.Column(db.String(200))
    count = db.Column(db.Integer)

    def __init__(self, long_url=None):
        self.long_url = long_url
        self.count = 0

    def __repr__(self):
        return '<Link: {self.long_url}, {self.short_postfix}, {self.count}>'.format(self=self)
