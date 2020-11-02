from flask_restful import Resource, abort, marshal_with, fields

from links_transform.shemas import LinksSchema


class LinksStat(Resource):
    @marshal_with({'count': fields.Integer})
    def get(self, short_postfix):
        ls = LinksSchema()
        errors = ls.validate({"short_postfix":short_postfix})
        if errors:
            abort(400, message=str(errors))
        link = ls.load({"short_postfix":short_postfix})
        if not link.long_url:
            abort(404, message="Link {} doesn't exist".format(short_postfix))
        if not link:
            abort(404, message="Link {} doesn't exist".format(short_postfix))
        return link
