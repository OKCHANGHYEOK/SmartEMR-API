from fastapi import Depends
from .BaseRouter import router
from Schemas.DataResponse import DataResponse
from Schemas.InsuranceDTO import Insurance_Req, Insurance_Res
from Services.Domain import InsuranceService

class InsuranceRouter():
    @router.post("/GetInsurance", response_model=DataResponse[Insurance_Res])
    async def GetInsurance(request : Insurance_Req, service : InsuranceService = Depends(InsuranceService)):
        return await service.GetInsurance(request)
    