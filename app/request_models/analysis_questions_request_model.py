from enum import Enum

from pydantic import BaseModel, Field


class FilterOperation(str, Enum):
    eq = 'eq'
    gt = 'gt'
    lt = 'lt'


class QueryFilter(BaseModel):
    col_name: str
    operation: FilterOperation = Field('eq', alias='operation')
    value: str


class AnalysisQuestionData(BaseModel):
    analysis_type: str

    class Config:
        schema_extra = {
            'example': {
                'analysis_type': 'HOW_HOW'
            }
        }


class AnalysisQuestionDataId(BaseModel):
    kaizen_analysis_question_id: str

    class Config:
        schema_extra = {
            'example': {
                'kaizen_analysis_question_id': '1fd8c744-d3ef-4879-b44e-dd58ae8f5435'
            }
        }
