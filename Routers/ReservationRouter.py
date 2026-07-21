from fastapi import Depends
from .BaseRouter import router
from Schemas.DataResponse import DataResponse
from Schemas.ReservationDTO import Reservation_Req, Reservation_Res
from Services.Domain import ReservationService

class ReservationRouter():
    @router.post("/GetReservation", response_model=DataResponse[Reservation_Res])
    async def GetReservation(request : Reservation_Req, service : ReservationService = Depends(ReservationService)):
        return await service.GetReservation(request)
    
    @router.post("/SetReservation", response_model=DataResponse[Reservation_Res])
    async def SetReservation(request : Reservation_Req, service : ReservationService = Depends(ReservationService)):
        return await service.SetReservation(request)