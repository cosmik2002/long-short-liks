from flask import request
from flask_restful import Resource, abort, marshal_with, fields
from werkzeug.utils import redirect

from links_transform import db, BaseN
from links_transform.models import Links
from links_transform.shemas import LinksSchema


class LinksResource(Resource):
    def __init__(self):
        self.digit_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def get(self, short_postfix):
        id = BaseN.BaseNToDec(short_postfix, self.digit_set)
        link = Links.query.get(id)
        if not link:
            abort(404, message="Link {} doesn't exist".format(short_postfix))
        link.count = link.count + 1
        db.session.commit()
        return redirect(link.long)

    @marshal_with({'short': fields.String})
    def put(self):
        ls = LinksSchema()
        link = ls.load(request.form)
        db.session.add(link)
        db.session.flush()
        link.short = BaseN.DecToBaseN(link.id, self.digit_set)
        db.session.commit()
        return link

