from fastapi import APIRouter, Depends
from Schemas.DataResponse import DataResponse
from Schemas.PatientDTO import Patient_Req, Patient_Res
from Services.Domain import PatientService

router = APIRouter()

class PatientRouter():
    def __init__(self, _service : PatientService = Depends(PatientService)):
        self.service = _service

    @router.post("/GetPatient", response_model=DataResponse[Patient_Res])
    async def GetPatient(self, request : Patient_Req):
        return await self.service.GetPatient(request)
    
    @router.post("/SetPatient", response_model=DataResponse[Patient_Res])
    async def SetPatient(self, request : Patient_Req):
        return await self.service.SetPatient(request)