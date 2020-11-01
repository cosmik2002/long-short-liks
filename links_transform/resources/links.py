from flask import request, url_for
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
        return redirect(link.long_url)

    def put(self):
        ls = LinksSchema()
        errors = ls.validate(request.form)
        if errors:
            abort(400, message=str(errors))
        link = ls.load(request.form)
        db.session.add(link)
        db.session.flush()
        link.short_postfix = BaseN.DecToBaseN(link.id, self.digit_set)
        db.session.commit()
        short_link = url_for("linksresource", short_postfix=link.short_postfix, _external=True)
        return {"short_link":short_link}

