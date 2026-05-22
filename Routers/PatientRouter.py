from fastapi import APIRouter, Depends
from Schemas.DataResponse import DataResponse
from Schemas.PatientDTO import Patient_Req, Patient_Res
from Services.Domain import PatientService

router = APIRouter()

class PatientRouter():
    @router.post("/GetPatient", response_model=DataResponse[Patient_Res])
    async def GetPatient(request : Patient_Req, service : PatientService = Depends(PatientService)):
        await service.GetPatient(request)