from marshmallow import Schema


class BaseSchema(Schema):
    __abstract__ = True
