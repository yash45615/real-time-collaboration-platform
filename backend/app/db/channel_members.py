from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer

from app.db.database import Base


class ChannelMember(Base):
    __tablename__ = "channel_members"

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

    joined_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )