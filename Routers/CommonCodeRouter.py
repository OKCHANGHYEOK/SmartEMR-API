from fastapi import APIRouter, Depends
from .BaseRouter import router
from Schemas.CommonCodeDTO import CommonCode_Req, CommonCode_Res
from Schemas.DataResponse import DataResponse
from Services.Domain import CommonCodeService

class CommonCodeRouter():
    @router.post("/GetCommonCode", response_model=DataResponse[CommonCode_Res])
    async def GetCommonCode(request : CommonCode_Req, service : CommonCodeService = Depends(CommonCodeService)):
        return await service.GetCommonCode(request)