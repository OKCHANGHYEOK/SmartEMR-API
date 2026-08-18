from fastapi import Depends
from .BaseRouter import router
from app.Schemas.DataResponse import DataResponse
from app.Schemas.InsuranceDTO import Insurance_Req, Insurance_Res
from app.Services.Domain import InsuranceService

class InsuranceRouter():
    @router.post("/GetInsurance", response_model=DataResponse[Insurance_Res])
    async def GetInsurance(request : Insurance_Req, service : InsuranceService = Depends(InsuranceService)):
        return await service.GetInsurance(request)

    @router.post("/GetRecentInsurance", response_model=DataResponse[Insurance_Res])
    async def GetRecentInsurance(request : Insurance_Req, service : InsuranceService = Depends(InsuranceService)):
        return await service.GetRecentInsurance(request)

    @router.post("/SetInsurance", response_model=DataResponse[Insurance_Res])
    async def SetInsurance(request : Insurance_Req, service : InsuranceService = Depends(InsuranceService)):
        return await service.SetInsurance(request)
    