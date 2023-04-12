from marshmallow import post_load

from app.models import Kaizen
from app.serializers.base_schema import BaseSchema


class KaizenSchema(BaseSchema):
    class Meta:
        fields = tuple(Kaizen.__table__.columns.keys())

