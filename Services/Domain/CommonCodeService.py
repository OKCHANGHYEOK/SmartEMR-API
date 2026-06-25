from fastapi import Depends
from Entities.CommonCode import CommonCode
from Services.Domain import BaseService
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Schemas.DataResponse import DataResponse
from Schemas.CommonCodeDTO import CommonCode_Req, CommonCode_Res
from Common import eSP
from Exceptions import ApiException

class CommonCodeService(BaseService):
    def __init__(self, _authenticatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenticatedUserService

    async def GetCommonCode(self, request : CommonCode_Req) -> DataResponse[CommonCode_Res]:
        item = CommonCode()

        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("올바르지 않은 유저입니다.", res_code=404)

        item.CCC_Cd = request.CCC_Cd
        item.CCG_Cd = request.CCG_Cd
        item.CCI_Cd = request.CCI_Cd

        ret : list[CommonCode_Res] = await self.DbContext.GetItems[CommonCode_Res](eSP.proc_CommonCode_GetCommonCode, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)

        return DataResponse[CommonCode_Res].CreateJsonResult(
            items = ret,
            message= self.DbContext.retMessage
        )