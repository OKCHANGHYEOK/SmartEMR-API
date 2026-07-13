from fastapi import APIRouter, Depends
from Schemas.DataResponse import DataResponse
from Schemas.PayDTO import Pay_Req, Pay_Res
from Services.Domain import PayService

router = APIRouter()

class PayRouter():
    @router.post("/GetPay", response_model=DataResponse[Pay_Res])
    async def GetPay(request : Pay_Req, service : PayService = Depends(PayService)):
        return await service.GetPay(request)
    
    @router.post("/SetPay", response_model=DataResponse[Pay_Res])
    async def SetPay(request : Pay_Req, service : PayService = Depends(PayService))
        return await service.SetPay(request)
