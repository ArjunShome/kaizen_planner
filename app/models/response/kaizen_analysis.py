from sqlalchemy import Column
from sqlalchemy import String, Index, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditMixin, UpdateMixin
from app.models.info import KaizenAnalysisQuestion
from app.models.response import Kaizen


class KaizenAnalysis(BaseModel, AuditMixin, UpdateMixin):
    """ The table to record all the kaizen analysis completed """

    __tablename__ = "kaizen_analysis"
    __table_args__ = (
        Index("idx_kaizen_analysis_kaizen_id", "kaizen_id"),
        {"schema": "response"},
    )

    kaizen_id = Column(UUID(as_uuid=True), ForeignKey(Kaizen.id))
    analysis_question_id = Column(UUID(as_uuid=True), ForeignKey(KaizenAnalysisQuestion.id))
    response = Column(String(512), nullable=False)
