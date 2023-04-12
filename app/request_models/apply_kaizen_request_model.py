from enum import Enum

from pydantic import BaseModel, Field
from app.models.enum_model import KaizenType


class FilterOperation(str, Enum):
    eq = 'eq'
    gt = 'gt'
    lt = 'lt'


class QueryFilter(BaseModel):
    col_name: str
    operation: FilterOperation = Field('eq', alias='operation')
    value: str


class ApplyKaizenData(BaseModel):
    user_id: str
    kaizen_type: KaizenType
    title: str

    class Config:
        schema_extra = {
            'example': {
                'user_id': 'N089',
                'kaizen_type': 'proactive',
                'title': 'Kaizen Planner'
            }
        }

