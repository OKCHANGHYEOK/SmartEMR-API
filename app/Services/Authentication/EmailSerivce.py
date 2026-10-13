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
from app.Schemas.DataResponse import DataResponse
from app.Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from app.Schemas.EmailVerificationDTO import EmailVerification_Req, EmailVerification_Res
from app.Services.Authentication.HashService import HashService
from app.Entities.MemberUser import MemberUser
from app.Entities.EmailVerification import EmailVerification
from app.Exceptions.ApiException import ApiException

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

    async def RequestVerifyCode(self, recipient : str, verify_code : str, dbContext : AppDBContext = AppDBContext()) -> DataResponse[EmailVerification_Res]:
        getMUR = MemberUser()
        getMUR.MUR_Email = recipient

        retMUR : MemberUser_Res = await dbContext.GetItem[MemberUser_Res](eSP.proc_MemberUser_GetMemberUser, getMUR)

        if retMUR and retMUR.MUR_Idx > 0:
            raise ApiException("이미 등록된 이메일입니다.\n이메일 변경후 다시 시도해주세요.")

        getEV = EmailVerification()
        getEV.EV_Email = recipient
        getEV.EV_Purpose = 'SIGNUP'

        retEV : EmailVerification_Res = await dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_GetEmailVerification, getEV)

        if retEV:
            lastSendDate = datetime.strptime(retEV.EV_CreatedAt, "%Y-%m-%d %H:%M:%S")

            diff = datetime.now() - lastSendDate

            if diff.seconds <= 60:
                raise ApiException("인증요청은 1분이내에 재요청할 수 없습니다.\n잠시 후 다시 시도해주세요.")
        
        subject = "[SmartEMR] 이메일 인증코드 안내"
        body = (
            "안녕하세요. SmartEMR입니다.\n\n"
            f"이메일 인증코드는 [{verify_code}] 입니다.\n"
            "인증코드 유효시간은 10분입니다.\n"
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
            
            return DataResponse[EmailVerification_Res].CreateJsonResult(item=retEV, message=dbContext.retMessage)
        
        except (smtplib.SMTPException, OSError):
            raise ApiException("이메일 발송에 실패했습니다.")

    async def VerifyCheck(request : EmailVerification_Req, dbContext : AppDBContext = AppDBContext()) -> DataResponse[EmailVerification_Res]:
        item = EmailVerification()
        item.EV_Email = request.EV_Email
        item.EV_Purpose = 'SIGNUP'

        ret : EmailVerification_Res = await dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_GetEmailVerificationByVerify, item)

        if not ret or dbContext.retIsSuccess == False:
            raise ApiException("이미 인증된 코드이거나 인증요청이 만료되었습니다.")

        isSuccess = HashService.VerifyVerificationCode(request.EV_CodeOrigin, ret.EV_CodeHash)

        if not isSuccess:
            raise ApiException("인증코드가 올바르지 않습니다.")

        setEV = EmailVerification()
        setEV.EV_Idx = ret.EV_Idx
        setEV.EV_IsVerified = True

        retEV : EmailVerification_Res = await dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_SetEmailVerification, setEV)

        if not retEV or dbContext.retIsSuccess == False:
            raise ApiException(dbContext.retMessage)

        return DataResponse[EmailVerification_Res].CreateJsonResult(item=ret)

