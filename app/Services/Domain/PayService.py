from fastapi import Depends
from app.Exceptions.ApiException import ApiException
from app.Entities.Pay import Pay
from app.Entities.Reception import Reception
from app.Services.Domain import BaseService
from app.Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from app.Schemas.DataResponse import DataResponse
from app.Schemas.PayDTO import Pay_Req, Pay_Res
from app.Common import eSP

class PayService(BaseService):
    def __init__(self, _authenicatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserService

    async def GetPay(self, request : Pay_Req) -> DataResponse[Pay_Res]:
        item : Pay = Pay()

        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx
        
        item.PAY_Idx = request.PAY_Idx
        item.PAT_Idx = request.PAT_Idx
        item.CST_Idx = request.CST_Idx

        item.CST_Status = request.CST_Status
        item.PAY_Status = request.PAY_Status
        item.PAY_YYMMDD = request.PAY_YYMMDD
        item.sDay = request.sDay
        item.eDay = request.eDay

        item.Keyword = request.Keyword
        item.SortField = request.SortField
        item.SortDir = request.SortDir
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        
        ret : list[Pay_Res] = await self.DbContext.GetItems[Pay_Res](eSP.proc_Pay_GetPay, item)

        if self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)

        return DataResponse[Pay_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)
    
    async def SetPay(self, request : Pay_Req) -> DataResponse[Pay_Res]:
        item : Pay = Pay()

        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")
        
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx
        
        item.PAY_Idx = request.PAY_Idx
        item.PAT_Idx = request.PAT_Idx
        item.CST_Idx = request.CST_Idx
        
        item.PAY_InsuredPrice = request.PAY_InsuredPrice
        item.PAY_NonInsuredPrice = request.PAY_NonInsuredPrice
        item.PAY_OwnPatientPrice = request.PAY_OwnPatientPrice
        item.PAY_TotalPrice = request.PAY_TotalPrice
        item.PAY_PaidPrice = request.PAY_PaidPrice
        item.PAY_RemainPrice = request.PAY_RemainPrice
        item.PAY_Memo = request.PAY_Memo
        item.PAY_IsValid = request.PAY_IsValid

        ret : Pay_Res = await self.DbContext.GetItem[Pay_Res](eSP.proc_Pay_SetPay, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException("수납 저장에 실패했습니다.")
        
        return DataResponse[Pay_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)

    async def CancelPay(self, request : Pay_Req) -> DataResponse[Pay_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")
        
        item : Pay = Pay()
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx
        item.PAY_Idx = request.PAY_Idx

        ret : Pay_Res = await self.DbContext.GetItem[Pay_Res](eSP.proc_Pay_CancelPay, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException("수납 취소에 실패했습니다.")
        
        return DataResponse[Pay_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)