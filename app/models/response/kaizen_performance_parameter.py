from sqlalchemy import Column
from sqlalchemy import String, Index, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditMixin, UpdateMixin
from app.models.enum_model import KaizenParameterType
from app.models.response import Kaizen


class KaizenPerfParam(BaseModel, AuditMixin, UpdateMixin):
    """ The master table for the Kaizen Application having the basic Kaizen related information and all associations """

    __tablename__ = "kaizen_perf_param"
    __table_args__ = (
        Index("idx_kaizen_perf_param_kaizen_id", "kaizen_id"),
        {"schema": "response"},
    )

    kaizen_id = Column(UUID(as_uuid=True), ForeignKey(Kaizen.id))
    parameter_type = Column(Enum(KaizenParameterType), nullable=True)
    parameter_description = Column(String(256), nullable=True)
