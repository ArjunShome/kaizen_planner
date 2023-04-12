from marshmallow import post_dump

from app.models.info import KaizenQuestion
from app.serializers.base_schema import BaseSchema


class KaizenQuestionSchema(BaseSchema):
    class Meta:
        fields = tuple(KaizenQuestion.__table__.columns.keys())

