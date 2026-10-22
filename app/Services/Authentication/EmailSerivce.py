import asyncio
import os
import smtplib

from datetime import datetime, timedelta
from email.message import EmailMessage
from email.headerregistry import Address
from fastapi import Depends

from app.Config import settings
from app.Common import Common
from app.Common.eSP import eSP
from app.Infrastructure.AppDBContext import AppDBContext
from app.Schemas.DataResponse import DataResponse
from app.Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from app.Schemas.EmailVerificationDTO import EmailVerification_Req, EmailVerification_Res
from app.Services.Authentication.HashService import HashService
from app.Services.Domain.BaseService import BaseService
from app.Entities.MemberUser import MemberUser
from app.Entities.EmailVerification import EmailVerification
from app.Exceptions.ApiException import ApiException

request_timeout = 10

class EmailService(BaseService):
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

    async def RequestVerifyCode(self, request : EmailVerification_Req) -> DataResponse[EmailVerification_Res]:
        if not request.EV_Email:
            raise ApiException("이메일이 올바르지 않습니다.")
        
        if request.EV_Purpose not in ['SIGNUP', 'FINDID', 'FINDPW']:
            raise ApiException("인증목적이 올바르지 않습니다.")
        
        if request.EV_Purpose == 'SIGNUP' and await self.exists_user('', '', request.EV_Email):
            raise ApiException("이미 가입된 이메일입니다.")

        if request.EV_Purpose == 'FINDID' and not await self.exists_user('', request.MUR_Name, request.EV_Email):
            raise ApiException("가입 정보를 찾을 수 없습니다. 입력하신 정보를 확인해주세요.")
        
        if request.EV_Purpose == 'FINDPW' and not await self.exists_user(request.MUR_Id, request.MUR_Name, request.EV_Email):
            raise ApiException("가입 정보를 찾을 수 없습니다. 입력하신 정보를 확인해주세요.")

        getEV = EmailVerification()
        getEV.EV_Email = request.EV_Email
        getEV.EV_Purpose = request.EV_Purpose

        retEV : EmailVerification_Res = await self._dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_GetEmailVerification, getEV)

        if retEV:
            lastSendDate = datetime.strptime(retEV.EV_CreatedAt, "%Y-%m-%d %H:%M:%S")

            diff = datetime.now() - lastSendDate

            if diff.seconds <= 60:
                raise ApiException("인증요청은 1분이내에 재요청할 수 없습니다.\n잠시 후 다시 시도해주세요.")
        
        verify_code = Common.GenerateVerificationCode()
        
        subject = f"[SmartEMR] {'회원가입' if request.EV_Purpose == 'SIGNUP' else '아이디 찾기' if request.EV_Purpose == 'FINDID' else '비밀번호 찾기'} 인증코드 안내"
        body = (
            "안녕하세요. SmartEMR입니다.\n\n"
            f"이메일 인증코드는 [{verify_code}] 입니다.\n"
            "인증코드 유효시간은 10분입니다.\n"
            "본인이 요청하지 않았다면 이 메일을 무시하셔도 됩니다."
        )

        try:
            setEV = EmailVerification()
            setEV.EV_Idx = 0
            setEV.EV_Purpose = request.EV_Purpose
            setEV.EV_Email = request.EV_Email
            setEV.EV_CodeHash = HashService.HashVerificationCode(verify_code)
            setEV.EV_CreatedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            setEV.EV_ExpiredAt = (datetime.now() + timedelta(minutes=request_timeout)).strftime('%Y-%m-%d %H:%M:%S')
            setEV.EV_IsVerified = 'False'
            setEV.EV_IsValid = 'True'

            retEV : EmailVerification_Res = await self._dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_SetEmailVerification, setEV)

            if not retEV or self._dbContext.retIsSuccess == False:
                raise ApiException("이메일 인증 요청을 저장하지 못했습니다.")

            await asyncio.to_thread(
                self.send_email_sync,
                request.EV_Email,
                subject,
                body
            )
            
            return DataResponse[EmailVerification_Res].CreateJsonResult(item=retEV, message=self._dbContext.retMessage)
        
        except (smtplib.SMTPException, OSError):
            raise ApiException("이메일 발송에 실패했습니다.")

    async def VerifyCheck(request : EmailVerification_Req, dbContext : AppDBContext = AppDBContext()) -> DataResponse[EmailVerification_Res]:
        item = EmailVerification()
        item.EV_Email = request.EV_Email
        item.EV_Purpose = request.EV_Purpose

        ret : EmailVerification_Res = await dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_GetEmailVerificationByVerify, item)

        if not ret or dbContext.retIsSuccess == False:
            raise ApiException("인증코드가 올바르지 않습니다.")

        isSuccess = HashService.VerifyVerificationCode(request.EV_CodeOrigin, ret.EV_CodeHash)

        if not isSuccess:
            raise ApiException("인증코드가 올바르지 않습니다.")

        if ret.EV_ExpiredAt < datetime.now().strftime('%Y-%m-%d %H:%M:%S'):
            raise ApiException("인증코드가 만료되었습니다. 다시 인증요청을 진행해주세요.")

        setEV = EmailVerification()
        setEV.EV_Idx = ret.EV_Idx
        setEV.EV_IsVerified = True

        retEV : EmailVerification_Res = await dbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_SetEmailVerification, setEV)

        if not retEV or dbContext.retIsSuccess == False:
            raise ApiException(dbContext.retMessage)

        return DataResponse[EmailVerification_Res].CreateJsonResult(item=ret)

    async def exists_user(self, id : str, name : str, email : str) -> bool:
        item = MemberUser()
        item.MUR_Id = id
        item.MUR_Name = name
        item.MUR_Email = email

        ret : MemberUser_Res = await self._dbContext.GetItem[MemberUser_Res](eSP.proc_MemberUser_GetMemberUser, item)

        if not ret or self._dbContext.retIsSuccess == False:
            return False
        
        return True