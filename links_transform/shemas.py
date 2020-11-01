from marshmallow import fields

from links_transform import ma
from links_transform.models import Links


class LinksSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Links
        load_instance = True

    id = ma.auto_field()
    long_url = fields.URL()
    short_postfix = ma.auto_field()
    count = ma.auto_field()


