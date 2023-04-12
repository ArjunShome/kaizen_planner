from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/kaizen_planner'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine, expire_on_commit=False)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    def set_attributes(self, values):
        for key, value in values.items():
            if (hasattr(self, key) and ((isinstance(value, str) and value)
                                        or (isinstance(value, (bool, int, float, list))))):
                setattr(self, key, value)


class AuditMixin(Base):
    __abstract__ = True

    created_on = Column(DateTime(timezone=True), default=datetime.utcnow)
    created_by = Column(String(128), nullable=True)


class UpdateMixin(Base):
    __abstract__ = True
    modified_on = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    modified_by = Column(String(128), nullable=True)
