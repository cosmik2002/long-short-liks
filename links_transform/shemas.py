from links_transform import ma
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class LinksSchema(ma.Schema):
    class Meta:
        model = Links
        load_instance = True

    id = auto_field()
    long = auto_field()
    short = auto_field()
    count = auto_field()


