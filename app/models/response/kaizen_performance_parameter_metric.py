from sqlalchemy import Column
from sqlalchemy import String, Index, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditMixin, UpdateMixin
from app.models.enum_model import KaizenPerformanceMetric
from app.models.response import KaizenPerfParam


class KaizenPerfParamMetric(BaseModel, AuditMixin, UpdateMixin):
    """ The master table for the Kaizen Application having the basic Kaizen related information and all associations """

    __tablename__ = "kaizen_perf_param_metric"
    __table_args__ = (
        Index("idx_kaizen_perf_param_metric_kaizen_perf_param_id", "kaizen_perf_param_id"),
        {"schema": "response"},
    )

    kaizen_perf_param_id = Column(UUID(as_uuid=True), ForeignKey(KaizenPerfParam.id))
    metric = Column(Enum(KaizenPerformanceMetric), nullable=False)
    performance_before = Column(String(256), nullable=False)
    performance_target = Column(String(256), nullable=False)
    performance_after = Column(String(256), nullable=False)
