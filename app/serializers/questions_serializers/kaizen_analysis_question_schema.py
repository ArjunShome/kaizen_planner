from marshmallow import post_load

from app.models.info import KaizenAnalysisQuestion
from app.serializers.base_schema import BaseSchema


class KaizenAnalysisQuestionSchema(BaseSchema):
    class Meta:
        fields = tuple(KaizenAnalysisQuestion.__table__.columns.keys())

