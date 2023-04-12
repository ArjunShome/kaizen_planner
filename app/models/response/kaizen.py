from sqlalchemy import Column
from sqlalchemy import String, Index, Enum, ARRAY, DateTime

from app.models.base_model import BaseModel, AuditMixin, UpdateMixin
from app.models.enum_model import KaizenStatus, KaizenSource, KaizenType


class Kaizen(BaseModel, AuditMixin, UpdateMixin):
    """ The master table for the Kaizen Application having the basic Kaizen related information and all associations """

    __tablename__ = "kaizen"
    __table_args__ = (
        Index("idx_kaizen_user_id", "user_id"),
        {"schema": "response"},
    )

    user_id = Column(String(128), nullable=False)
    type = Column(Enum(KaizenType), nullable=True)
    title = Column(String(1024), nullable=True)
    problem_statement = Column(String(2048), nullable=True)
    status = Column(Enum(KaizenStatus), nullable=True)
    source = Column(Enum(KaizenSource), nullable=True)
    owner = Column(String(256), nullable=True)
    team_members = Column(ARRAY(String), nullable=True)
    department_name = Column(String(256), nullable=True)
    project_name = Column(String(256), nullable=True)
    kaizen_start_date = Column(DateTime(timezone=True))
    kaizen_end_date = Column(DateTime(timezone=True))
