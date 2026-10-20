from fastapi import Depends
from app.Common import eSP
from app.Common import Common
from app.Services.Domain import BaseService
from app.Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from app.Schemas.DataResponse import DataResponse
from app.Schemas.OrderDTO import Order_Req, Order_Res
from app.Exceptions.ApiException import ApiException
from app.Entities.Order import Order

class SugaService(BaseService):
    def __init__(self, _authenicatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserService

    async def GetSugaCategory(self, request : Order_Req) -> DataResponse[Order_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item = Order()
        item.SUGAC_Cd = request.SUGAC_Cd

        ret = await self.DbContext.GetItems[Order_Res](eSP.proc_Suga_GetSugaCategory, item)

        if self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)

        return DataResponse[Order_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)