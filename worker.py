import os
from email.mime.text import MIMEText

from dotenv import load_dotenv
from rococo.messaging import RabbitMqConnection

from app.mailing.smtp import SMTPService

load_dotenv()


def get_email_service():
    return SMTPService(
        host=os.environ.get("SMTP_HOST"),
        port=os.environ.get("SMTP_PORT"),
        username=os.environ.get("SMTP_USERNAME"),
        password=os.environ.get("SMTP_PASSWORD"),
    )


def send_recovery_code(data: dict):
    base_url = "http://localhost:5000"
    recovery_token = data.get("token")
    service = get_email_service()

    restore_password_url = f"{base_url}/#/auth/reset_password/{recovery_token}"

    msg = MIMEText(f"Please reset your password. {restore_password_url}")
    msg["Subject"] = "Reset Password"
    msg["From"] = "rococo@rococo.com"

    service.send_email(
        {
            "from": "rococo@rococo.com",
            "to": ["user@example.com"],
            "message": msg.as_string(),
        }
    )
    return True


with RabbitMqConnection(
    host=os.environ.get("RABBITMQ_HOST", "localhost"),
    port=int(os.environ.get("RABBITMQ_PORT", "5672")),
    username=os.environ.get("RABBITMQ_USERNAME", "guest"),
    password=os.environ.get("RABBITMQ_PASSWORD", "guest"),
    virtual_host="/",
) as connection:
    connection.consume_messages("recovery_code", send_recovery_code)
