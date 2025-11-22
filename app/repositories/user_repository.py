# app/repositories/user_repository.py

from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User # Mantén este
from app.schemas.user import UserCreate # Mantén este

# ELIMINA la importación de get_password_hash de aquí.


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> Optional[User]:
        # ... (código get_by_email)
        return self.db.query(User).filter(User.email == email).first()

    def create(self, usuario_in: UserCreate) -> User:
        # 👇 IMPORTAR DENTRO DEL MÉTODO
        from app.core.security import get_password_hash
        
        hashed_password = get_password_hash(usuario_in.password)

        db_user = User(
            # ... (código de creación de usuario)
            email=usuario_in.email,
            full_name=usuario_in.full_name,
            hashed_password=hashed_password,
            identificacion=usuario_in.identificacion,
            nombre=usuario_in.nombre,
            apellido=usuario_in.apellido,
            programa=usuario_in.programa,
            semestre=usuario_in.semestre,
            telefono=usuario_in.telefono,
            is_active=True,
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user