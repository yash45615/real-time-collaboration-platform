from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.db.models import User
from app.db.workspace_models import (
    Workspace,
    WorkspaceMember,
)
from app.schemas.workspace import (
    WorkspaceCreate,
    WorkspaceMemberCreate,
    WorkspaceMemberResponse,
    WorkspaceResponse,
)


router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"],
)


@router.post(
    "",
    response_model=WorkspaceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_workspace(
    workspace_data: WorkspaceCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    workspace = Workspace(
        name=workspace_data.name,
        description=workspace_data.description,
        owner_id=current_user.id,
    )

    db.add(workspace)
    db.commit()
    db.refresh(workspace)

    membership = WorkspaceMember(
        workspace_id=workspace.id,
        user_id=current_user.id,
        role="admin",
    )

    db.add(membership)
    db.commit()

    return workspace


@router.get(
    "",
    response_model=list[WorkspaceResponse],
)
def list_workspaces(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    workspaces = (
        db.query(Workspace)
        .join(
            WorkspaceMember,
            WorkspaceMember.workspace_id == Workspace.id,
        )
        .filter(
            WorkspaceMember.user_id == current_user.id
        )
        .all()
    )

    return workspaces


@router.post(
    "/{workspace_id}/members",
    response_model=WorkspaceMemberResponse,
)
def add_member(
    workspace_id: int,
    member_data: WorkspaceMemberCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    workspace = (
        db.query(Workspace)
        .filter(Workspace.id == workspace_id)
        .first()
    )

    if workspace is None:
        raise HTTPException(
            status_code=404,
            detail="Workspace not found",
        )

    if workspace.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Only workspace owner can add members",
        )

    user = (
        db.query(User)
        .filter(User.id == member_data.user_id)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    existing = (
        db.query(WorkspaceMember)
        .filter(
            WorkspaceMember.workspace_id == workspace_id,
            WorkspaceMember.user_id == member_data.user_id,
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already belongs to workspace",
        )

    if member_data.role not in ["admin", "member"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid role",
        )

    membership = WorkspaceMember(
        workspace_id=workspace_id,
        user_id=member_data.user_id,
        role=member_data.role,
    )

    db.add(membership)
    db.commit()
    db.refresh(membership)

    return membership