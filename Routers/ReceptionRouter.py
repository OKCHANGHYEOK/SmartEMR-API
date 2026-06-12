from fastapi import APIRouter, Depends
from Schemas.DataResponse import DataResponse
from Schemas.ReceptionDTO import Reception_Req, Reception_Res
from Services.Domain import ReceptionService

router = APIRouter()

class ReceptionRouter():
    @router.post("/GetReception", response_model=DataResponse[Reception_Res])
    async def GetReception(request : Reception_Req, service : ReceptionService = Depends(ReceptionService)):
        return await service.GetReception(request)
    
    @router.post("/SetReception", response_model=DataResponse[Reception_Res])
    async def SetReception(request : Reception_Req, service : ReceptionService = Depends(ReceptionService)):
        return await service.SetReception(request)