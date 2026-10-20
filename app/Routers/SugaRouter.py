from fastapi import APIRouter, Depends
from app.Schemas.DataResponse import DataResponse
from app.Schemas.OrderDTO import Order_Req, Order_Res
from app.Services.Domain import SugaService

router = APIRouter()

class SugaRouter():
    @router.post("/GetSugaCategory", response_model=DataResponse[Order_Res])
    async def GetSugaCategory(request : Order_Req, service : SugaService = Depends(SugaService)):
        return await service.GetSugaCategory(request)