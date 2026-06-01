from Entities.ChartCommonCode import ChartCommonCode
from Services.Domain import BaseService
from Schemas.DataResponse import DataResponse
from Schemas.ChartCommonCodeDTO import ChartCommonCode_Req, ChartCommonCode_Res
from Common import eSP
from Exceptions import ApiException

class ChartCommonCodeService(BaseService):
    async def GetChartCommonCode(self, request : ChartCommonCode_Req) -> DataResponse[ChartCommonCode_Res]:
        item = ChartCommonCode()

        item.CCCG_Cd = request.CCCG_Cd
        item.CCC_Cd = request.CCC_Cd

        ret : list[ChartCommonCode_Res] = await self.DbContext.GetItems(eSP.proc_ChartCommonCode_GetChartCommonCode, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)

        return DataResponse[ChartCommonCode_Res] (
            items = ret,
            Message=self.DbContext.retMessage
        )