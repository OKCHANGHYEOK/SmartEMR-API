from fastapi import APIRouter, Depends
from Schemas.ChartCommonCodeDTO import ChartCommonCode_Req, ChartCommonCode_Res
from Schemas.DataResponse import DataResponse
from Services.Domain import ChartCommonCodeService

router = APIRouter()

class ChartCommonCodeRouter():
    @router.post("/GetChartCommonCode", response_model=DataResponse[ChartCommonCode_Res])
    async def GetChartCommonCode(request : ChartCommonCode_Req, service : ChartCommonCodeService = Depends(ChartCommonCodeService)):
        return await service.GetChartCommonCode(request)