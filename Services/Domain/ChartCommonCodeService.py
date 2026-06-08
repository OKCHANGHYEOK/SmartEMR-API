from fastapi import Depends
from Entities.ChartCommonCode import ChartCommonCode
from Services.Domain import BaseService
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Schemas.DataResponse import DataResponse
from Schemas.ChartCommonCodeDTO import ChartCommonCode_Req, ChartCommonCode_Res
from Common import eSP
from Exceptions import ApiException

class ChartCommonCodeService(BaseService):
    def __init__(self, _authenticatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenticatedUserService

    async def GetChartCommonCode(self, request : ChartCommonCode_Req) -> DataResponse[ChartCommonCode_Res]:
        item = ChartCommonCode()

        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("올바르지 않은 유저입니다.", res_code=404)

        item.CCCM_Cd = request.CCCM_Cd
        item.CCCG_Cd = request.CCCG_Cd
        item.CCC_Cd = request.CCC_Cd

        ret : list[ChartCommonCode_Res] = await self.DbContext.GetItems(eSP.proc_ChartCommonCode_GetChartCommonCode, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)

        return DataResponse[ChartCommonCode_Res].CreateJsonResult(
            items = ret,
            message= self.DbContext.retMessage
        )