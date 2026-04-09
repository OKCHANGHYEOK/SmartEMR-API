from Entities.MemberUser import MemberUser
from Services.Authentication import HashService
from Services.Domain import BaseSerivce
from Schemas.DataResponse import DataResponse
from Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from Common import eSP
from Exceptions import ApiException

class MemberUserService(BaseSerivce):
   async def GetMemberUserForLogin(self, request : MemberUser_Req) -> DataResponse[MemberUser_Res]:
      item = MemberUser()

      item.MUR_Id = request.MUR_Id

      ret : MemberUser_Res = await self.DbContext.GetItem(eSP.proc_MemberUser_GetMemberUserForLogin, item)

      if ret is None or self.DbContext.retIsSuccess == False:
         raise ApiException(self.DbContext.retMessage)
      
      return DataResponse[MemberUser_Res](Item=ret, Message=self.DbContext.retMessage, IsSuccess=self.DbContext.retIsSuccess)
   
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

      ret : MemberUser_Res = await self.DbContext.GetItem(eSP.proc_MemberUser_SetMemberUser, item)

      if ret is None or self.DbContext.retIsSuccess == False:
         raise ApiException(self.DbContext.retMessage)
      
      return DataResponse[MemberUser_Res].CreateJsonResult(item=ret)

