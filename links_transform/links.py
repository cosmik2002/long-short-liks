from flask import request
from flask_restful import Resource

from links_transform import db
from links_transform.models import Links
from links_transform.shemas import LinksSchema

class LinksResource(Resource):
    def __init__(self):
        print ('init')

    def get(self):
        l = Links.query.get(1)
        ls = LinksSchema()
        a = ls.dump(l)
        b = ls.jsonify(l)
        return ls.jsonify(l)

    def put(self):
        ls = LinksSchema()
        l = ls.load(request.form)
        db.session.add(l)
        db.session.commit()
        return ""