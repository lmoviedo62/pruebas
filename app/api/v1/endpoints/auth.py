from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import secrets

from app.api.deps import get_db, get_current_user
from app.schemas.user import UserCreate, UserOut, UserLogin
from app.schemas.auth import Token
from app.repositories.user_repository import UserRepository
from app.services.email import email_service
from app.services.auth import verify_password, create_access_token
from app.core.security import get_password_hash
from app.models.user import User

router = APIRouter(tags=["auth"])


@router.post("/register", response_model=UserOut)
def register_user(usuario_in: UserCreate, db: Session = Depends(get_db)):
    """
    Registro de nuevo usuario.
    Valida correo institucional y que no exista previamente.
    """
    repo = UserRepository(db)

    # Validar correo institucional
    if not usuario_in.email.endswith("@ucatolica.edu.co"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo debe ser institucional (@ucatolica.edu.co)."
        )

    # Comprobar si el correo ya existe
    existing = repo.get_by_email(usuario_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya está registrado.",
        )
    
    # Comprobar si la identificación ya existe
    existing_id = db.query(User).filter(User.identificacion == usuario_in.identificacion).first()
    if existing_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La identificación ya está registrada en el sistema.",
        )

    user = repo.create(usuario_in)
    print(f"✅ Usuario registrado: {user.email}")
    return user


@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Login de usuario.
    Valida credenciales y retorna token JWT.
    """
    print(f"🔐 Intento de login: {credentials.email}")
    
    # Validar correo institucional
    if not credentials.email.endswith("@ucatolica.edu.co"):
        print(f"❌ Correo no institucional: {credentials.email}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo debe ser institucional (@ucatolica.edu.co)."
        )
    
    # Buscar usuario
    user = db.query(User).filter(User.email == credentials.email).first()
    
    if not user:
        print(f"❌ Usuario no encontrado: {credentials.email}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Este correo no está registrado. Por favor regístrate primero."
        )
    
    print(f"✅ Usuario encontrado: {user.email}")
    
    # Verificar contraseña
    password_valid = verify_password(credentials.password, user.hashed_password)
    print(f"🔑 Contraseña válida: {password_valid}")
    
    if not password_valid:
        print(f"❌ Contraseña incorrecta para: {credentials.email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta."
        )
    
    # Crear token de acceso
    access_token = create_access_token(data={"sub": user.email})
    print(f"✅ Token generado para: {user.email}")
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/logout")
def logout(current_user: User = Depends(get_current_user)):
    """
    Cierra la sesión del usuario actual.
    En el frontend se debe eliminar el token del localStorage.
    """
    print(f"👋 Logout: {current_user.email}")
    return {
        "message": "Sesión cerrada exitosamente",
        "user": current_user.email
    }


@router.post("/forgot-password")
def forgot_password(
    email: str = Query(..., description="Correo institucional del usuario"),
    db: Session = Depends(get_db)
):
    """
    Endpoint para solicitar recuperación de contraseña.
    Genera un token único y envía el correo con el enlace de reseteo.
    """
    print(f"🔒 Solicitud de recuperación para: {email}")
    
    # Validar que sea correo institucional
    if not email.endswith("@ucatolica.edu.co"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo debe ser institucional (@ucatolica.edu.co)"
        )
    
    # Buscar usuario por email
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Este correo no está registrado. Por favor regístrate primero."
        )
    
    # Generar token único de recuperación (32 caracteres seguros)
    reset_token = secrets.token_urlsafe(32)
    
    # Guardar token y fecha de expiración en la BD (1 hora de validez)
    user.reset_token = reset_token
    user.reset_token_expires = datetime.utcnow() + timedelta(hours=1)
    db.commit()
    
    print(f"✅ Token de recuperación generado para: {email}")
    
    # Enviar correo con el enlace de recuperación
    try:
        email_service.send_password_reset_email(
            to_email=user.email,
            nombre=user.nombre,
            reset_token=reset_token
        )
        print(f"📧 Correo de recuperación enviado a: {email}")
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al enviar el correo. Por favor intenta más tarde."
        )
    
    return {
        "message": f"Se ha enviado un correo a {email} con instrucciones para recuperar tu contraseña."
    }


@router.post("/reset-password")
def reset_password(
    token: str = Query(..., description="Token de recuperación"),
    new_password: str = Query(..., min_length=8, description="Nueva contraseña"),
    db: Session = Depends(get_db)
):
    """
    Endpoint para restablecer la contraseña usando el token enviado por correo.
    """
    print(f"🔑 Intento de reseteo con token: {token[:10]}...")
    
    # Buscar usuario con el token válido
    user = db.query(User).filter(
        User.reset_token == token,
        User.reset_token_expires > datetime.utcnow()
    ).first()
    
    if not user:
        print(f"❌ Token inválido o expirado")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token inválido o expirado. Solicita un nuevo enlace de recuperación."
        )
    
    # Actualizar contraseña
    user.hashed_password = get_password_hash(new_password)
    
    # Limpiar token de recuperación
    user.reset_token = None
    user.reset_token_expires = None
    
    db.commit()
    
    print(f"✅ Contraseña actualizada para: {user.email}")
    
    return {
        "message": "Contraseña actualizada correctamente. Ya puedes iniciar sesión con tu nueva contraseña."
    }