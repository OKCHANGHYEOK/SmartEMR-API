from fastapi import Depends
from app.Exceptions.ApiException import ApiException
from app.Entities.Pay import Pay
from app.Entities.PayItem import PayItem
from app.Entities.Reception import Reception
from app.Services.Domain import BaseService
from app.Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from app.Schemas.DataResponse import DataResponse
from app.Schemas.PayDTO import Pay_Req, Pay_Res
from app.Schemas.PayItemDTO import PayItem_Req, PayItem_Res
from app.Common import eSP

class PayItemService(BaseService):
    def __init__(self, _authenicatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserService

    async def GetPayItem(self, request : PayItem_Req) -> DataResponse[PayItem_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : PayItem = PayItem()
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.PAT_Idx = request.PAT_Idx
        item.PAY_Idx = request.PAY_Idx
        item.PAYI_Type = request.PAYI_Type
        item.PAYI_Method = request.PAYI_Method
        item.PAYI_YYMMDD = request.PAYI_YYMMDD

        item.Keyword = request.Keyword
        item.SortField = request.SortField
        item.SortDir = request.SortDir
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex

        ret : list[PayItem_Res] = await self.DbContext.GetItems[PayItem_Res](eSP.proc_PayItem_GetPayItem, item)

        if self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[PayItem_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)

    async def SetPayItem(self, request : PayItem_Req) -> DataResponse[PayItem_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        # 수납 검증
        retPAY : Pay_Res = await self.DbContext.GetItem[Pay_Res](eSP.proc_Pay_GetPay, Pay(PAY_Idx = request.PAY_Idx))

        if retPAY is None:
            raise ApiException("수납 정보가 삭제되었거나 존재하지 않습니다.")

        item : PayItem = PayItem()
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.PAYI_Idx = request.PAYI_Idx
        item.PAY_Idx = request.PAY_Idx
        item.PAT_Idx = request.PAT_Idx
        item.PAYI_Type = request.PAYI_Type
        item.PAYI_Method = request.PAYI_Method
        item.PAYI_Price = request.PAYI_Price
        item.PAYI_Time = request.PAYI_Time
        item.PAYI_IsValid = request.PAYI_IsValid

        ret : list[PayItem_Res] = await self.DbContext.GetItem[PayItem_Res](eSP.proc_PayItem_SetPayItem, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)

        setPAY : Pay = Pay()
        setPAY.MEM_Idx = user.MEM_Idx
        setPAY.MUR_Idx = user.MUR_Idx
        setPAY.PAY_Idx = request.PAY_Idx

        retPAY : Pay_Res = await self.DbContext.GetItem[Pay_Res](eSP.proc_Pay_UpdatePayByPrice, setPAY)

        return DataResponse[PayItem_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)