from fastapi import Depends
from .BaseRouter import router
from app.Schemas.ConsultationOrderDTO import ConsultationOrder_Req, ConsultationOrder_Res
from app.Schemas.DataResponse import DataResponse
from app.Services.Domain import ConsultationOrderService

class ConsultationOrderRouter():
    @router.post("/GetConsultationOrder", response_model=DataResponse[ConsultationOrder_Res])
    async def GetConsultationOrder(request : ConsultationOrder_Req, service : ConsultationOrderService = Depends(ConsultationOrderService)):
        return await service.GetConsultationOrder(request)

    @router.post("/SetConsultationOrder", response_model=DataResponse[ConsultationOrder_Res])
    async def SetConsultationOrder(request : ConsultationOrder_Req, service : ConsultationOrderService = Depends(ConsultationOrderService)):
        return await service.SetConsultationOrder(request)
