from fastapi import APIRouter, Depends
from app.Schemas.DataResponse import DataResponse
from app.Schemas.PatientDTO import Patient_Req, Patient_Res
from app.Services.Domain import PatientService

router = APIRouter()

class PatientRouter():
    @router.post("/GetPatient", response_model=DataResponse[Patient_Res])
    async def GetPatient(request : Patient_Req, service : PatientService = Depends(PatientService)):
        return await service.GetPatient(request)
    
    @router.post("/SetPatient", response_model=DataResponse[Patient_Res])
    async def SetPatient(request : Patient_Req, service : PatientService = Depends(PatientService)):
        return await service.SetPatient(request)