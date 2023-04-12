from sqlalchemy import Column
from sqlalchemy import String, Index, Enum, Integer

from app.models.base_model import BaseModel
from app.models.enum_model import KaizenQuestionSegment, KaizenType


class KaizenQuestion(BaseModel):
    """ Kaizen Questions table having all the questions for applying a kaizen other than analysis type questions """

    __tablename__ = "kaizen_question"
    __table_args__ = (
        Index("idx_kaizen_question_question", "question"),
        {"schema": "info"},
    )

    question = Column(String(256), nullable=False)
    reference_table = Column(Enum(KaizenQuestionSegment), nullable=False)
    reference_table_column = Column(String(32), nullable=False)
    question_type = Column(Enum(KaizenType), nullable=False)
    question_stage = Column(String(32), nullable=False)
    sort_order = Column(Integer, nullable=False)
