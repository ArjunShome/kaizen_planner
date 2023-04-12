from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field
from typing import List


class FilterOperation(str, Enum):
    eq = 'eq'
    gt = 'gt'
    lt = 'lt'


class QueryFilter(BaseModel):
    col_name: str
    operation: FilterOperation = Field('eq', alias='operation')
    value: str


class QuestionData(BaseModel):
    kaizen_type: str
    question_stage: Optional[str]
    responses:List[dict]

    class Config:
        schema_extra = {
            'example': {
                'kaizen_type': 'PROACTIVE',
                'question_stage': 'Planning'
            }
        }

class QuestionDataId(BaseModel):
    kaizen_question_id: str

    class Config:
        schema_extra = {
            'example': {
                'kaizen_question_id': '48089a90-1cad-4eae-9548-16037e8d684c'
            }
        }
