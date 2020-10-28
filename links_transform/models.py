from sqlalchemy import Column, Integer, String
from links_transform.database import Base


class Links(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    short = Column(String(50), unique=True)
    long = Column(String(200))
    count = Column(Integer)

    def __init__(self, long=None, short=None):
        self.long = long
        self.short = short

    def __repr__(self):
        return '<Link: {self.long}, {self.short}, {self.count}>'.format(self=self)
