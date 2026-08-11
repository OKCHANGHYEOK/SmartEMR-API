from fastapi import Depends
from .BaseRouter import router
from Schemas.ConsultationDTO import Consultation_Req, Consultation_Res
from Schemas.DataResponse import DataResponse
from Services.Domain import ConsultationService

class ConsultationRouter():
    @router.post("/GetConsultation", response_model=DataResponse[Consultation_Res])
    async def GetConsultation(request : Consultation_Req, service : ConsultationService = Depends(ConsultationService)):
        return await service.GetConsultation(request)

    @router.post("/SetConsultation", response_model=DataResponse[Consultation_Res])
    async def SetConsultation(request : Consultation_Req, service : ConsultationService = Depends(ConsultationService)):
        return await service.SetConsultation(request)