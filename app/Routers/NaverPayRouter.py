from fastapi import APIRouter, Depends
from app.Schemas.DataResponse import DataResponse
from app.Schemas.NaverPayDTO import NaverPay_Req, NaverPay_Res
from app.Services.Domain import NaverPayService

router = APIRouter()

class NaverPayRouter:
    @router.post("/ApplyPayment", response_model=DataResponse[NaverPay_Res])
    async def ApplyPayment(request : NaverPay_Req, service : NaverPayService = Depends(NaverPayService)):
        return await service.ApplyPayment(request)
