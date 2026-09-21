from fastapi import Depends, HTTPException, status

from app.core.dependencies import get_current_user
from app.db.models import User


def require_admin(
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin permission required",
        )

    return current_user


def require_member(
    current_user: User = Depends(get_current_user),
):
    if current_user.role not in ["admin", "member"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Member permission required",
        )

    return current_user