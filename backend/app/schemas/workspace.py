from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WorkspaceCreate(BaseModel):
    name: str
    description: str | None = None


class WorkspaceResponse(BaseModel):
    id: int
    name: str
    description: str | None
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class WorkspaceMemberCreate(BaseModel):
    user_id: int
    role: str = "member"


class WorkspaceMemberResponse(BaseModel):
    id: int
    workspace_id: int
    user_id: int
    role: str
    joined_at: datetime

    model_config = ConfigDict(from_attributes=True)