from links_transform import ma
from links_transform.models import Links


class LinksSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Links
        load_instance = True

    id = ma.auto_field()
    long = ma.auto_field()
    short = ma.auto_field()
    count = ma.auto_field()


