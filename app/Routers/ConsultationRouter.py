from fastapi import Depends
from .BaseRouter import router
from app.Schemas.ConsultationDTO import Consultation_Req, Consultation_Res
from app.Schemas.DataResponse import DataResponse
from app.Services.Domain import ConsultationService

class ConsultationRouter():
    @router.post("/GetConsultation", response_model=DataResponse[Consultation_Res])
    async def GetConsultation(request : Consultation_Req, service : ConsultationService = Depends(ConsultationService)):
        return await service.GetConsultation(request)

    @router.post("/GetConsultationByRCP", response_model=DataResponse[Consultation_Res])
    async def GetConsultationByRCP(request : Consultation_Req, service : ConsultationService = Depends(ConsultationService)):
        return await service.GetConsultationByRCP(request)

    @router.post("/SetConsultation", response_model=DataResponse[Consultation_Res])
    async def SetConsultation(request : Consultation_Req, service : ConsultationService = Depends(ConsultationService)):
        return await service.SetConsultation(request)

    @router.post("/SetConsultationByCST", response_model=DataResponse[Consultation_Res])
    async def SetConsultationByCST(request : Consultation_Req, service : ConsultationService = Depends(ConsultationService)):
        return await service.SetConsultationByCST(request)