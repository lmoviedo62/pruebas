from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserOut, UserLogin
from app.repositories.user_repository import UserRepository

# ❌ ANTES: router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
# ✅ AHORA:
router = APIRouter(tags=["auth"])


@router.post("/register", response_model=UserOut)
def register_user(usuario_in: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)

    # comprobar si el correo ya existe
    existing = repo.get_by_email(usuario_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya está registrado.",
        )

    user = repo.create(usuario_in)
    return user
