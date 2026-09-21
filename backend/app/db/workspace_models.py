from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.db.database import Base


class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String,
        nullable=False,
    )

    description = Column(
        String,
        nullable=True,
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


class WorkspaceMember(Base):
    __tablename__ = "workspace_members"

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

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    role = Column(
        String,
        default="member",
        nullable=False,
    )

    joined_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )