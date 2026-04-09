from Entities.MemberUser import MemberUser
from Services.Domain import BaseSerivce
from Schemas.DataResponse import DataResponse
from Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from Common import eSP
from Exceptions import ApiException

class MemberUserService(BaseSerivce):
   async def GetMemberUserForLogin(self, request : MemberUser_Req) -> DataResponse[MemberUser_Res]:
      item = MemberUser()

      item.MUR_Id = request.MUR_Id
      item.MUR_Password = request.MUR_Password

      ret : MemberUser_Res = await self.DbContext.GetItem(eSP.proc_MemberUser_GetMemberUserForLogin, item)

      if ret is None or self.DbContext.retIsSuccess == False:
         raise ApiException(self.DbContext.retMessage)
      
      return DataResponse[MemberUser_Res](Item=ret)