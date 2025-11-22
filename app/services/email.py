from email.message import EmailMessage
import smtplib
from typing import Optional

from app.core.config import settings


class EmailService:
    """
    Servicio de correo (Patrón: Service Layer / Singleton por módulo).
    Se encarga de toda la lógica de envío de correos.
    """

    def __init__(self):
        self.host = settings.SMTP_HOST
        self.port = settings.SMTP_PORT
        self.username = settings.SMTP_USER
        self.password = settings.SMTP_PASSWORD
        self.use_tls = True

    def _send_email(
        self,
        to_email: str,
        subject: str,
        body: str,
        reply_to: Optional[str] = None,
    ) -> None:
        msg = EmailMessage()
        msg["From"] = self.username
        msg["To"] = to_email
        msg["Subject"] = subject
        if reply_to:
            msg["Reply-To"] = reply_to
        msg.set_content(body)

        with smtplib.SMTP(self.host, self.port) as server:
            if self.use_tls:
                server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)

    # --- Correos específicos para Serena ---

    def send_welcome_email(self, to_email: str, nombre: str) -> None:
        subject = "Bienvenido(a) a Serena 💜"
        body = (
            f"Hola {nombre},\n\n"
            "Gracias por registrarte en Serena, la plataforma de apoyo emocional "
            "para estudiantes de la Universidad Católica de Colombia.\n\n"
            "Desde ahora podrás usar el chat de apoyo, ejercicios de respiración "
            "y recursos de ayuda.\n\n"
            "Un abrazo,\n"
            "Equipo Serena"
        )
        self._send_email(to_email, subject, body)

    def send_sos_email(self, to_email: str, nombre: str, motivo: str) -> None:
        subject = "Solicitud de ayuda inmediata (Serena)"
        body = (
            f"Estudiante: {nombre}\n"
            f"Correo: {to_email}\n\n"
            f"Motivo reportado:\n{motivo}\n\n"
            "Por favor contactar a la mayor brevedad posible."
        )
        destinatario_bienestar = settings.SOS_EMAIL_DEST
        self._send_email(destinatario_bienestar, subject, body, reply_to=to_email)

    def send_password_reset_email(self, to_email: str, nombre: str, reset_token: str) -> None:
        """
        🆕 Envía correo con enlace de recuperación de contraseña
        """
        subject = "Recuperación de contraseña - Serena 🔒"
        
        # URL del enlace de recuperación (ajusta según tu dominio)
        reset_url = f"http://127.0.0.1:8000/reset-password?token={reset_token}"
        
        body = (
            f"Hola {nombre},\n\n"
            "Recibimos una solicitud para restablecer la contraseña de tu cuenta en Serena.\n\n"
            "Para crear una nueva contraseña, haz clic en el siguiente enlace:\n"
            f"{reset_url}\n\n"
            "⚠️ Este enlace es válido por 1 hora.\n\n"
            "Si no solicitaste este cambio, puedes ignorar este correo y tu contraseña permanecerá sin cambios.\n\n"
            "Equipo Serena 💜\n"
            "Universidad Católica de Colombia"
        )
        self._send_email(to_email, subject, body)


# Instancia única (Singleton a nivel de módulo)
email_service = EmailService()