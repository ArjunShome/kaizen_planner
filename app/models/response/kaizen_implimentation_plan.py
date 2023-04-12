from sqlalchemy import Column
from sqlalchemy import String, Index, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditMixin, UpdateMixin
from app.models.response import KaizenDevelopmentSolution


class KaizenImplementationPlan(BaseModel, AuditMixin, UpdateMixin):
    """ The table to record all the kaizen implementations for all the development plans considered"""

    __tablename__ = "kaizen_implementation_plan"
    __table_args__ = (
        Index("idx_kaizen_implementation_plan_development_solution_id", "development_solution_id"),
        {"schema": "response"},
    )

    development_solution_id = Column(UUID(as_uuid=True), ForeignKey(KaizenDevelopmentSolution.id))
    target_date = Column(DateTime(timezone=True))
    actual_date = Column(DateTime(timezone=True))
    improvement_action = Column(String(512), nullable=True)
    improvement_solution = Column(String(512), nullable=True)
