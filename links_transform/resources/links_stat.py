from flask_restful import Resource, abort, marshal_with, fields

from links_transform import BaseN
from links_transform.models import Links


class LinksStat(Resource):
    def __init__(self):
        self.digit_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @marshal_with({'count': fields.Integer})
    def get(self, short_postfix):
        id = BaseN.BaseNToDec(short_postfix, self.digit_set)
        link = Links.query.get(id)
        if not link:
            abort(404, message="Link {} doesn't exist".format(short_postfix))
        return link
