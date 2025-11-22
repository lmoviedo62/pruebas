from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from app.db.base_class import Base


class PasswordResetToken(Base):
    """
    Modelo para almacenar tokens de recuperación de contraseña.
    """
    __tablename__ = "password_reset_tokens"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, index=True)
    token = Column(String(255), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False, nullable=False)
    used_at = Column(DateTime, nullable=True)