from re import match

from flask import request, url_for
from flask_restful import Resource, abort, marshal_with, fields
from werkzeug.utils import redirect

from links_transform import db, BaseN
from links_transform.models import Links
from links_transform.shemas import LinksSchema


class LinksResource(Resource):

    def get(self, short_postfix):
        ls = LinksSchema()
        errors = ls.validate({"short_postfix":short_postfix})
        if errors:
            abort(400, message=str(errors))
        link = ls.load({"short_postfix":short_postfix})
        if not link.long_url:
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
        dump = ls.dump(link)
        db.session.commit()
        short_link = dump['short_link']
        return {"short_link":short_link}

