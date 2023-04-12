from sqlalchemy import Column
from sqlalchemy import String, Index, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditMixin, UpdateMixin
from app.models.response import Kaizen


class KaizenDevelopmentSolution(BaseModel, AuditMixin, UpdateMixin):
    """ The table to record all the kaizen development solutions considered """

    __tablename__ = "kaizen_development_solution"
    __table_args__ = (
        Index("idx_kaizen_development_solution_kaizen_id", "kaizen_id"),
        {"schema": "response"},
    )

    kaizen_id = Column(UUID(as_uuid=True), ForeignKey(Kaizen.id))
    aspect = Column(String(256), nullable=True)
    root_cause = Column(String(512), nullable=True)
    idea = Column(String(256), nullable=True)
    improvement_action = Column(String(256), nullable=True)
    improvement_action_owner = Column(String(256), nullable=True)
    improvement_outcome = Column(String(512), nullable=True)
