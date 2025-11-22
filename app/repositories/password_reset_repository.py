from typing import Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
import secrets

from app.models.password_reset import PasswordResetToken


class PasswordResetRepository:
    """
    Repositorio para gestionar tokens de recuperación de contraseña.
    Patrón: Repository Pattern
    """

    def __init__(self, db: Session):
        self.db = db

    def create_token(self, email: str) -> str:
        """
        Crea un token único para recuperación de contraseña.
        
        Reglas de negocio:
        - El token debe ser único y aleatorio (32 caracteres)
        - Expira en 1 hora
        - Solo puede haber un token activo por usuario
        """
        # Invalidar tokens anteriores del mismo usuario
        self.invalidate_user_tokens(email)

        # Generar token único
        token = secrets.token_urlsafe(32)
        
        # Fecha de expiración: 1 hora desde ahora
        expires_at = datetime.utcnow() + timedelta(hours=1)

        # Crear registro en la base de datos
        reset_token = PasswordResetToken(
            email=email,
            token=token,
            expires_at=expires_at,
            used=False
        )

        self.db.add(reset_token)
        self.db.commit()
        self.db.refresh(reset_token)

        return token

    def get_valid_token(self, token: str) -> Optional[PasswordResetToken]:
        """
        Obtiene un token si es válido (no usado y no expirado).
        
        Reglas de negocio:
        - El token debe existir
        - No debe haber sido usado
        - No debe estar expirado
        """
        reset_token = self.db.query(PasswordResetToken).filter(
            PasswordResetToken.token == token,
            PasswordResetToken.used == False,
            PasswordResetToken.expires_at > datetime.utcnow()
        ).first()

        return reset_token

    def mark_as_used(self, token: str) -> bool:
        """
        Marca un token como usado para que no pueda reutilizarse.
        
        Reglas de negocio:
        - Un token solo puede usarse una vez
        """
        reset_token = self.db.query(PasswordResetToken).filter(
            PasswordResetToken.token == token
        ).first()

        if reset_token:
            reset_token.used = True
            reset_token.used_at = datetime.utcnow()
            self.db.commit()
            return True
        return False

    def invalidate_user_tokens(self, email: str) -> None:
        """
        Invalida todos los tokens activos de un usuario.
        
        Reglas de negocio:
        - Al solicitar un nuevo token, los anteriores deben invalidarse
        """
        self.db.query(PasswordResetToken).filter(
            PasswordResetToken.email == email,
            PasswordResetToken.used == False
        ).update({"used": True, "used_at": datetime.utcnow()})
        self.db.commit()