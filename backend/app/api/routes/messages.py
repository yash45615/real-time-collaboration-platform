from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.channel_members import ChannelMember
from app.db.channel_models import Channel
from app.db.database import get_db
from app.db.message_models import Message
from app.db.models import User
from app.schemas.message import MessageCreate, MessageResponse


router = APIRouter(
    prefix="/channels",
    tags=["Messages"],
)


def check_channel_access(
    channel_id: int,
    user_id: int,
    db: Session,
):
    return (
        db.query(ChannelMember)
        .filter(
            ChannelMember.channel_id == channel_id,
            ChannelMember.user_id == user_id,
        )
        .first()
    )


@router.post(
    "/{channel_id}/messages",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_message(
    channel_id: int,
    message_data: MessageCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    channel = (
        db.query(Channel)
        .filter(Channel.id == channel_id)
        .first()
    )

    if channel is None:
        raise HTTPException(
            404,
            "Channel not found",
        )

    access = check_channel_access(
        channel_id,
        current_user.id,
        db,
    )

    if access is None:
        raise HTTPException(
            403,
            "You are not a channel member",
        )

    message = Message(
        channel_id=channel_id,
        user_id=current_user.id,
        content=message_data.content,
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message


@router.get(
    "/{channel_id}/messages",
    response_model=list[MessageResponse],
)
def message_history(
    channel_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    access = check_channel_access(
        channel_id,
        current_user.id,
        db,
    )

    if access is None:
        raise HTTPException(
            403,
            "You are not a channel member",
        )

    return (
        db.query(Message)
        .filter(Message.channel_id == channel_id)
        .order_by(Message.created_at.asc())
        .all()
    )