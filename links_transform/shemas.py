from re import match

from flask_marshmallow.fields import AbsoluteUrlFor
from marshmallow import fields, validate, pre_load, ValidationError, pre_dump

from links_transform import ma, BaseN
from links_transform.models import Links

digit_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class LinksSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Links
        load_instance = True

    id = ma.auto_field()
    long_url = fields.URL()
    short_postfix = fields.String(validate = validate.Regexp("^[{}]+$".format(digit_set)))
    count = ma.auto_field()
    short_link = AbsoluteUrlFor("linksresource", values=dict(short_postfix='<short_postfix>'))


    @pre_load
    def pre_process_postfix(self, data, **kwarg):
        if "short_postfix" in data and not "id" in data:
            if not match("^[{}]+$".format(digit_set), data['short_postfix']):
                raise  ValidationError("malformed url")
            id = BaseN.BaseNToDec(data['short_postfix'], digit_set)
            data['id'] = id
        return data

    @pre_dump
    def pre_dump_postfix(self, link, **kwargs):
        if not link.short_postfix and link.id:
            link.short_postfix = BaseN.DecToBaseN(link.id, digit_set)
        return link





