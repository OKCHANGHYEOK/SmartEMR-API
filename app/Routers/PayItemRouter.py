from fastapi import Depends
from .BaseRouter import router
from app.Schemas.DataResponse import DataResponse
from app.Schemas.PayItemDTO import PayItem_Req, PayItem_Res
from app.Services.Domain import PayItemService

class PayItemRouter():
    @router.post("/GetPayItem", response_model=DataResponse[PayItem_Res])
    async def GetPayItem(request : PayItem_Req, service : PayItemService = Depends(PayItemService)):
        return await service.GetPayItem(request)
    
    @router.post("/SetPay", response_model=DataResponse[PayItem_Res])
    async def SetPay(request : PayItem_Req, service : PayItemService = Depends(PayItemService)):
        return await service.SetPayItem(request)
