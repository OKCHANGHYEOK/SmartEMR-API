from fastapi import Depends
from app.Services.Authentication.HashService import HashService
from app.Services.Domain.BaseService import BaseService
from app.Schemas.DataResponse import DataResponse
from app.Schemas.EmailVerificationDTO import EmailVerification_Req, EmailVerification_Res
from app.Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from app.Entities.EmailVerification import EmailVerification
from app.Entities.MemberUser import MemberUser
from app.Common import eSP
from app.Exceptions import ApiException

class MemberUserService(BaseService):
   async def GetMemberUserByCheckDuplicateId(self, request : MemberUser_Req) -> DataResponse[MemberUser_Res]:
      item = MemberUser()

      item.MUR_Id = request.MUR_Id

      ret : MemberUser_Res = await self.DbContext.GetItem[MemberUser_Res](eSP.proc_MemberUser_GetMemberUser, item)

      if self.DbContext.retIsSuccess == False:
         raise ApiException(self.DbContext.retMessage)
      
      return DataResponse[MemberUser_Res](Item=ret, Message=self.DbContext.retMessage, IsSuccess=self.DbContext.retIsSuccess)
   
   async def GetMemberUserForLogin(self, request : MemberUser_Req) -> DataResponse[MemberUser_Res]:
      item = MemberUser()

      item.MUR_Idx = request.MUR_Idx
      item.MUR_Id = request.MUR_Id

      ret : MemberUser_Res = await self.DbContext.GetItem[MemberUser_Res](eSP.proc_MemberUser_GetMemberUserForLogin, item)

      if ret is None or self.DbContext.retIsSuccess == False:
         raise ApiException("아이디 또는 패스워드가 일치하지 않습니다.", status_code=401)
      
      return DataResponse[MemberUser_Res](Item=ret, Message=self.DbContext.retMessage, IsSuccess=self.DbContext.retIsSuccess)
   
   async def GetMemberUser(self, request : MemberUser_Req) -> DataResponse[MemberUser_Res]:
      item = MemberUser()

      item.MEM_Idx = request.MEM_Idx
      item.MUR_Idx = request.MUR_Idx
      item.MUR_Name = request.MUR_Name

      ret = await self.DbContext.GetItems[MemberUser_Res](eSP.proc_MemberUser_GetMemberUser, item)

      if ret is None or self.DbContext.retIsSuccess == False:
         raise ApiException(self.DbContext.retMessage)
      
      return DataResponse[MemberUser_Res].CreateJsonResult(items=ret)

   async def SetMemberUser(self, request : MemberUser_Req) -> DataResponse[MemberUser_Res]:
      item = MemberUser()

      item.MEM_Idx = request.MEM_Idx
      item.MUR_Idx = request.MUR_Idx
      item.MUR_Role = request.MUR_Role
      item.MUR_Id = request.MUR_Id 
      item.MUR_Name = request.MUR_Name
      item.MUR_Gender = request.MUR_Gender
      item.MUR_Address1 = request.MUR_Address1
      item.MUR_Address2 = request.MUR_Address2
      item.MUR_Address3 = request.MUR_Address3
      item.MUR_BirthYear = request.MUR_BirthYear
      item.MUR_BirthMonth = request.MUR_BirthMonth
      item.MUR_BirthDay = request.MUR_BirthDay  
      item.MUR_PhoneNum1 = request.MUR_PhoneNum1
      item.MUR_PhoneNum2 = request.MUR_PhoneNum2
      item.MUR_PhoneNum3 = request.MUR_PhoneNum3
      item.MUR_Email = request.MUR_Email
      item.MUR_IsValid = request.MUR_IsValid

      # 비밀번호 해시 처리
      if not item.MUR_Idx or item.MUR_Idx == 0:
         item.MUR_PassWord = HashService.HashPassword(request.MUR_PassWord)
      else:
         pass   

      ret = await self.DbContext.GetItem[MemberUser_Res](eSP.proc_MemberUser_SetMemberUser, item)

      if ret is None or self.DbContext.retIsSuccess == False:
         raise ApiException(self.DbContext.retMessage)
      
      return DataResponse[MemberUser_Res].CreateJsonResult(items=ret)

   async def SignUp(self, request : MemberUser_Req) -> DataResponse[MemberUser_Res]:
      if not request.MEM_Idx or request.MEM_Idx == 0:
         raise ApiException("회원사키값이 올바르지 않습니다.")
      
      retMUR : MemberUser_Res = await self.DbContext.GetItem[MemberUser_Res](eSP.proc_MemberUser_GetMemberUser, MemberUser(MUR_Id=request.MUR_Id))
      
      if retMUR and retMUR.MUR_Idx > 0:
         raise ApiException("이미 사용중인 아이디입니다. 아이디 변경후 다시 시도하세요.")

      if not request.EV_Idx_Verified:
         raise ApiException("이메일 본인인증을 완료하지 않았습니다. 본인인증후 다시 시도하세요.")

      getEV = EmailVerification()
      getEV.EV_Idx = request.EV_Idx_Verified
      getEV.EV_Email = request.MUR_Email
      getEV.EV_IsVerified = True

      retEV : EmailVerification_Res = await self.DbContext.GetItem[EmailVerification_Res](eSP.proc_EmailVerification_GetEmailVerification, getEV)

      if not retEV or self.DbContext.retIsSuccess == False:
         raise ApiException("본인인증을 진행한 이메일이 아닙니다.")
      
      item : MemberUser = MemberUser()
      item.MEM_Idx = request.MEM_Idx
      item.MUR_Idx = 0
      item.MUR_Name = request.MUR_Name
      item.MUR_Id = request.MUR_Id
      item.MUR_PassWord = HashService.HashPassword(request.MUR_PassWord)
      item.MUR_Department = request.MUR_Department
      item.MUR_Role =  request.MUR_Role if request.MUR_Role else "USR"
      item.MUR_JobCode = request.MUR_JobCode
      item.MUR_LicenseNo = request.MUR_LicenseNo
      item.MUR_Email = request.MUR_Email
      item.MUR_IsValid = True
      
      ret : MemberUser_Res = await self.DbContext.GetItem[MemberUser_Res](eSP.proc_MemberUser_SetMemberUser, item)
      
      if not ret or self.DbContext.retIsSuccess == False:
         raise ApiException(self.DbContext.retMessage)

      return DataResponse[MemberUser_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)      
      
       