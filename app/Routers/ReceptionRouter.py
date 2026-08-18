from fastapi import Depends
from .BaseRouter import router
from app.Schemas.DataResponse import DataResponse
from app.Schemas.ReceptionDTO import Reception_Req, Reception_Res
from app.Schemas.ReceptionBoardDTO import ReceptionBoard_Req, ReceptionBoard_Res
from app.Schemas.ReservationDTO import Reservation_Req 
from app.Services.Domain import ReceptionService

class ReceptionRouter():
    @router.post("/GetReception", response_model=DataResponse[Reception_Res])
    async def GetReception(request : Reception_Req, service : ReceptionService = Depends(ReceptionService)):
        return await service.GetReception(request)
    
    @router.post("/GetReceptionBoard", response_model=DataResponse[ReceptionBoard_Res]) 
    async def GetReceptionBoard(request : ReceptionBoard_Req, service : ReceptionService = Depends(ReceptionService)):
        return await service.GetReceptionBoard(request)
    
    @router.post("/SetReception", response_model=DataResponse[Reception_Res])
    async def SetReception(request : Reception_Req, service : ReceptionService = Depends(ReceptionService)):
        return await service.SetReception(request)

    @router.post("/SetReceptionByRES", response_model=DataResponse[Reception_Res])
    async def SetReceptionByRES(request : Reservation_Req, service : ReceptionService = Depends(ReceptionService)):
        return await service.SetReceptionByRES(request)

    @router.post("/CancelReception", response_model=DataResponse[Reception_Res])
    async def CancelReception(request : Reception_Req, service : ReceptionService = Depends(ReceptionService)):
        return await service.CancelReception(request)