from sqlalchemy import Column
from sqlalchemy import String, Index, Enum

from app.models.base_model import BaseModel, AuditMixin, UpdateMixin
from app.models.enum_model import KaizenAnalysisType


class KaizenAnalysisQuestion(BaseModel):
    """ Kaizen Analysis Questions to be verified"""

    __tablename__ = "kaizen_analysis_question"
    __table_args__ = (
        Index("idx_kaizen_analysis_question_question", "question"),
        {"schema": "info"},
    )

    question = Column(String(256), nullable=False)
    analysis_type = Column(Enum(KaizenAnalysisType), nullable=False)
