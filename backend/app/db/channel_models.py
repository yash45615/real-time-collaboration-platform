from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.db.database import Base


class Channel(Base):
    __tablename__ = "channels"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id"),
        nullable=False,
    )

    name = Column(
        String,
        nullable=False,
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )