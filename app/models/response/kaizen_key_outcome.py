from sqlalchemy import Column
from sqlalchemy import String, Index, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditMixin, UpdateMixin
from app.models.enum_model import KaizenOutcomeType
from app.models.response import Kaizen


class KaizenKeyOutcome(BaseModel, AuditMixin, UpdateMixin):
    """ The table for recording the kaizen outcomes """

    __tablename__ = "kaizen_key_outcome"
    __table_args__ = (
        Index("kaizen_key_outcome_kaizen_id", "kaizen_id"),
        {"schema": "response"},
    )

    kaizen_id = Column(UUID(as_uuid=True), ForeignKey(Kaizen.id))
    outcome = Column(String(256), nullable=False)
    outcome_type = Column(Enum(KaizenOutcomeType), nullable=False)
