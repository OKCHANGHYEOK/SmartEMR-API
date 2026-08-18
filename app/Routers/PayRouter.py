from fastapi import Depends
from .BaseRouter import router
from app.Schemas.DataResponse import DataResponse
from app.Schemas.PayDTO import Pay_Req, Pay_Res
from app.Services.Domain import PayService

class PayRouter():
    @router.post("/GetPay", response_model=DataResponse[Pay_Res])
    async def GetPay(request : Pay_Req, service : PayService = Depends(PayService)):
        return await service.GetPay(request)
    
    @router.post("/SetPay", response_model=DataResponse[Pay_Res])
    async def SetPay(request : Pay_Req, service : PayService = Depends(PayService)):
        return await service.SetPay(request)
