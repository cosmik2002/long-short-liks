from flask_restful import Resource
from links_transform.models import Links

class LinksResource(Resource):
    def __init__(self):
        print ('init')

    def get(self):
        l = Links.query.get(1)
        return {'long': l.long}
