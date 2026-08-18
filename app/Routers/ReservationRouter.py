from fastapi import Depends
from .BaseRouter import router
from app.Schemas.DataResponse import DataResponse
from app.Schemas.ReservationDTO import Reservation_Req, Reservation_Res
from app.Services.Domain import ReservationService

class ReservationRouter():
    @router.post("/GetReservation", response_model=DataResponse[Reservation_Res])
    async def GetReservation(request : Reservation_Req, service : ReservationService = Depends(ReservationService)):
        return await service.GetReservation(request)
    
    @router.post("/SetReservation", response_model=DataResponse[Reservation_Res])
    async def SetReservation(request : Reservation_Req, service : ReservationService = Depends(ReservationService)):
        return await service.SetReservation(request)

    @router.post("/SetReservationByStatus", response_model=DataResponse[Reservation_Res])
    async def SetReservationByStatus(request : Reservation_Req, service : ReservationService = Depends(ReservationService)):
        return await service.SetReservationByStatus(request)

    @router.post("/MoveReservationDate", response_model=DataResponse[Reservation_Res])
    async def MoveReservationDate(request : Reservation_Req, service : ReservationService = Depends(ReservationService)):
        return await service.MoveReservationDate(request)