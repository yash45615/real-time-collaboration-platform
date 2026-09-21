from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.channel_members import ChannelMember
from app.db.channel_models import Channel
from app.db.database import get_db
from app.db.models import User
from app.db.workspace_models import Workspace, WorkspaceMember
from app.schemas.channel import (
    ChannelCreate,
    ChannelMemberCreate,
    ChannelResponse,
)


router = APIRouter(
    prefix="/channels",
    tags=["Channels"],
)


def check_workspace_member(
    workspace_id: int,
    user_id: int,
    db: Session,
):
    membership = (
        db.query(WorkspaceMember)
        .filter(
            WorkspaceMember.workspace_id == workspace_id,
            WorkspaceMember.user_id == user_id,
        )
        .first()
    )

    return membership


@router.post(
    "/workspace/{workspace_id}",
    response_model=ChannelResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_channel(
    workspace_id: int,
    channel_data: ChannelCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    workspace = (
        db.query(Workspace)
        .filter(Workspace.id == workspace_id)
        .first()
    )

    if workspace is None:
        raise HTTPException(404, "Workspace not found")

    membership = check_workspace_member(
        workspace_id,
        current_user.id,
        db,
    )

    if membership is None:
        raise HTTPException(
            403,
            "You are not a workspace member",
        )

    channel = Channel(
        workspace_id=workspace_id,
        name=channel_data.name,
        created_by=current_user.id,
    )

    db.add(channel)
    db.commit()
    db.refresh(channel)

    channel_member = ChannelMember(
        channel_id=channel.id,
        user_id=current_user.id,
    )

    db.add(channel_member)
    db.commit()

    return channel


@router.get(
    "/workspace/{workspace_id}",
    response_model=list[ChannelResponse],
)
def list_channels(
    workspace_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    membership = check_workspace_member(
        workspace_id,
        current_user.id,
        db,
    )

    if membership is None:
        raise HTTPException(
            403,
            "You are not a workspace member",
        )

    return (
        db.query(Channel)
        .filter(Channel.workspace_id == workspace_id)
        .all()
    )


@router.post(
    "/{channel_id}/members",
)
def add_channel_member(
    channel_id: int,
    member_data: ChannelMemberCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    channel = (
        db.query(Channel)
        .filter(Channel.id == channel_id)
        .first()
    )

    if channel is None:
        raise HTTPException(404, "Channel not found")

    workspace_membership = check_workspace_member(
        channel.workspace_id,
        current_user.id,
        db,
    )

    if workspace_membership is None:
        raise HTTPException(
            403,
            "You are not a workspace member",
        )

    target_workspace_membership = check_workspace_member(
        channel.workspace_id,
        member_data.user_id,
        db,
    )

    if target_workspace_membership is None:
        raise HTTPException(
            400,
            "User must belong to workspace first",
        )

    existing = (
        db.query(ChannelMember)
        .filter(
            ChannelMember.channel_id == channel_id,
            ChannelMember.user_id == member_data.user_id,
        )
        .first()
    )

    if existing:
        raise HTTPException(
            400,
            "User already belongs to channel",
        )

    membership = ChannelMember(
        channel_id=channel_id,
        user_id=member_data.user_id,
    )

    db.add(membership)
    db.commit()

    return {
        "message": "User added to channel",
        "channel_id": channel_id,
        "user_id": member_data.user_id,
    }