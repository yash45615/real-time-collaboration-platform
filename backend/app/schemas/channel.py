from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ChannelCreate(BaseModel):
    name: str


class ChannelResponse(BaseModel):
    id: int
    workspace_id: int
    name: str
    created_by: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ChannelMemberCreate(BaseModel):
    user_id: int