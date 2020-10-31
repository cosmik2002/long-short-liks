from links_transform import db


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(50))
    long = db.Column(db.String(200))
    count = db.Column(db.Integer)

    def __init__(self, long=None):
        self.long = long
        self.count = 0

    def __repr__(self):
        return '<Link: {self.long}, {self.short}, {self.count}>'.format(self=self)
