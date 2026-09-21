from datetime import datetime

from pydantic import BaseModel, ConfigDict


class MessageCreate(BaseModel):
    content: str


class MessageResponse(BaseModel):
    id: int
    channel_id: int
    user_id: int
    content: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)