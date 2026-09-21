from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text

from app.db.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    channel_id = Column(
        Integer,
        ForeignKey("channels.id"),
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    content = Column(
        Text,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )