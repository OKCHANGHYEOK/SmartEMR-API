from fastapi import APIRouter, Depends
from app.Schemas.DataResponse import DataResponse
from app.Schemas.OrderDTO import Order_Req, Order_Res
from app.Services.Domain import OrderService

router = APIRouter()

class OrderRouter():
    @router.post("/GetOrder", response_model=DataResponse[Order_Res])
    async def GetOrder(request : Order_Req, service : OrderService = Depends(OrderService)):
        return await service.GetOrder(request)