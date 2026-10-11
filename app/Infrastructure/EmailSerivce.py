import asyncio
import os
import smtplib

from datetime import datetime, timedelta
from email.message import EmailMessage
from email.headerregistry import Address
from fastapi import Depends
from app.Config import settings
from app.Common.eSP import eSP
from app.Infrastructure.AppDBContext import AppDBContext
from app.Exceptions.ApiException import ApiException
from app.Entities.EmailVerification import EmailVerification
from app.Schemas.DataResponse import DataResponse
from app.Schemas.EmailVerificationDTO import EmailVerification_Req, EmailVerification_Res
from app.Services.Authentication.HashService import HashService

request_timeout = 10

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
            request_timeout
        ) as smtp:
            smtp.starttls()
            smtp.login(
                settings.email.smtp_user,
                settings.email.smtp_password
            )
            smtp.send_message(message)

    async def SendVerificationCodeAsync(self, recipient : str, verify_code : str, dbContext : AppDBContext = AppDBContext()) -> bool:
        subject = "[SmartEMR] 이메일 인증코드 안내"
        body = (
            "안녕하세요. SmartEMR입니다.\n\n"
            f"이메일 인증코드는 [{verify_code}] 입니다.\n"
            "인증코드는 제한된 시간 동안만 유효합니다.\n"
            "본인이 요청하지 않았다면 이 메일을 무시하셔도 됩니다."
        )

        try:
            setEV = EmailVerification()
            setEV.EV_Idx = 0
            setEV.EV_Purpose = 'SIGNUP'
            setEV.EV_Email = recipient
            setEV.EV_CodeHash = HashService.HashVerificationCode(verify_code)
            setEV.EV_CreatedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            setEV.EV_ExpiredAt = (datetime.now() + timedelta(minutes=request_timeout)).strftime('%Y-%m-%d %H:%M:%S')
            setEV.EV_IsVerified = 'False'
            setEV.EV_IsValid = 'True'

            retEV : EmailVerification_Res = await dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_SetEmailVerification, setEV)

            if not retEV or dbContext.retIsSuccess == False:
                raise ApiException("이메일 인증 요청을 저장하지 못했습니다.")


            await asyncio.to_thread(
                self.send_email_sync,
                recipient,
                subject,
                body
            )
            
            return True
        
        except (smtplib.SMTPException, OSError):
            raise ApiException("이메일 발송에 실패했습니다.")

    async def VerifyCheck(request : EmailVerification_Req, dbContext : AppDBContext = AppDBContext()) -> DataResponse[EmailVerification_Res]:
        item = EmailVerification_Req()
        item.EV_Email = request.EV_Email
        item.EV_Purpose = 'SIGNUP'
        item.EV_CodeOrigin = request.EV_CodeOrigin

        ret : EmailVerification_Res = await dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_GetEmailVerification, item)

        if not ret or dbContext.retIsSuccess == False:
            raise ApiException("인증요청이 존재하지 않습니다.")

        isSuccess = HashService.HashVerificationCode(item.EV_CodeOrigin, ret.EV_CodeHash)

        if not isSuccess:
            raise ApiException("인증코드가 올바르지 않습니다.")

        return DataResponse[EmailVerification_Res].CreateDefaultResult()

