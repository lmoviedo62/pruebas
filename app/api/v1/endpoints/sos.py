from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.services.email import email_service
from app.models.user import User

router = APIRouter()

@router.get("/resources", response_model=list[dict])
def list_resources():
    return [
        {
            "nombre": "Línea Nacional de Emergencias",
            "tipo": "Teléfono",
            "contacto": "123",
            "region": "Colombia",
        },
        {
            "nombre": "Bienestar Universitario",
            "tipo": "Correo",
            "contacto": "bienestar@ucatolica.edu.co",
            "region": "Universidad",
        },
    ]


@router.post("/send-urgency")
def send_urgency_email(
    urgency_data: dict = Body(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Envía un correo de urgencia a Bienestar Universitario
    """
    try:
        urgency_type = urgency_data.get("urgency_type")
        message = urgency_data.get("message")
        safe_situation = urgency_data.get("safe_situation")
        
        # Construir el cuerpo del correo
        email_body = f"""
═══════════════════════════════════════════════
🆘 SOLICITUD DE ATENCIÓN URGENTE - SERENA
═══════════════════════════════════════════════

📋 INFORMACIÓN DEL ESTUDIANTE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nombre: {current_user.nombre} {current_user.apellido}
Identificación: {current_user.identificacion}
Correo: {current_user.email}
Programa: {current_user.programa}
Semestre: {current_user.semestre}
Teléfono: {current_user.telefono}

🆘 TIPO DE URGENCIA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{urgency_type}

💬 DESCRIPCIÓN DE LA SITUACIÓN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{message}

🛡️ ¿ESTÁ EN LUGAR SEGURO?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{safe_situation}

⏰ FECHA Y HORA DE SOLICITUD:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{urgency_data.get('timestamp', 'N/A')}

═══════════════════════════════════════════════
⚠️ ESTA ES UNA SOLICITUD URGENTE
Por favor, contactar al estudiante lo antes posible.
═══════════════════════════════════════════════

Generado automáticamente por Serena - Sistema de Apoyo Emocional UCC
        """
        
        # Enviar correo
        email_service._send_email(
            to_email="bienestaruccpi@gmail.com",
            subject=f"🆘 SOLICITUD URGENTE - {current_user.nombre} {current_user.apellido}",
            body=email_body,
            reply_to=current_user.email
        )
        
        return {
            "success": True,
            "message": "Solicitud de urgencia enviada correctamente"
        }
        
    except Exception as e:
        print(f"❌ Error al enviar correo de urgencia: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error al enviar la solicitud de urgencia"
        )