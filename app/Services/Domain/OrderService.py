from fastapi import Depends
from app.Common import eSP
from app.Common import Common
from app.Services.Domain import BaseService
from app.Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from app.Schemas.DataResponse import DataResponse
from app.Schemas.OrderDTO import Order_Req, Order_Res
from app.Exceptions.ApiException import ApiException
from app.Entities.Order import Order

class OrderService(BaseService):
    def __init__(self, _authenicatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserService

    async def GetOrder(self, request : Order_Req) -> DataResponse[Order_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : Order = Order()
        item.ORD_SugaCode = request.ORD_SugaCode
        item.ORD_ClassCode = request.ORD_ClassCode
        item.ORD_InsuranceType = request.ORD_InsuranceType
        item.ORD_SurgeryType = request.ORD_SurgeryType
        item.ORDC_Cd = request.ORDC_Cd
        item.ORD_IsUse = request.ORD_IsUse
        item.ORD_IsQuickOrder = request.ORD_IsQuickOrder

        item.Keyword = request.Keyword
        item.SortField = request.SortField
        item.SortDir = request.SortDir
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex

        ret : list[Order_Res] = await self.DbContext.GetItems[Order_Res](eSP.proc_Order_GetOrder, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException("오더 조회에 실패했습니다.")

        return DataResponse[Order_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage, totalCount=self.DbContext.retCount)