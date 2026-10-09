import asyncio
import os
import smtplib

from email.message import EmailMessage
from email.headerregistry import Address
from app.Config import settings
from app.Exceptions.ApiException import ApiException

class EmailService:
    @staticmethod
    def send_email_sync(recipient : str, subject : str, body : str) -> bool:
        message = EmailMessage()
        message["Subject"] = subject
        message["From"] = settings.email.smtp_from
        message["To"] = recipient

        message.set_content(body)

        with smtplib.SMTP(
            settings.email.smtp_host,
            settings.email.smtp_port,
            timeout=10
        ) as smtp:
            smtp.starttls()
            smtp.login(
                settings.email.smtp_user,
                settings.email.smtp_password
            )
            smtp.send_message(message)

    async def SendVerificationCodeAsync(self, recipient : str, verify_code : str) -> bool:
        subject = "[SmartEMR] 이메일 인증코드 안내"
        body = (
            "안녕하세요. SmartEMR입니다.\n\n"
            f"이메일 인증코드는 [{verify_code}] 입니다.\n"
            "인증코드는 제한된 시간 동안만 유효합니다.\n"
            "본인이 요청하지 않았다면 이 메일을 무시하셔도 됩니다."
        )

        try:
            await asyncio.to_thread(
                self.send_email_sync,
                recipient,
                subject,
                body
            )
            
            return True
        
        except (smtplib.SMTPException, OSError):
            raise ApiException("이메일 발송에 실패했습니다.")