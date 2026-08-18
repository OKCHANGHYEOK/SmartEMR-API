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

        item.PAY_Status = request.PAY_Status
        item.PAY_YYMMDD = request.PAY_YYMMDD

        item.SortField = request.SortField
        item.SortDir = request.SortDir
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        
        ret : list[Pay_Res] = await self.DbContext.GetItems[Pay_Res](eSP.proc_Pay_GetPay, item)

        if not ret or self.DbContext.retIsSuccess == False:
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
        
        item.PAY_AMOUNT_TOT = request.PAY_AMOUNT_TOT
        item.PAY_AMOUNT_INSURED = request.PAY_AMOUNT_INSURED
        item.PAY_AMOUNT_NONINSURED = request.PAY_AMOUNT_NONINSURED
        item.PAY_AMOUNT_PATIENT = request.PAY_AMOUNT_PATIENT
        item.PAY_AMOUNT_PAID = request.PAY_AMOUNT_PAID
        item.PAY_AMOUNT_REMAIN = request.PAY_AMOUNT_REMAIN
        item.PAY_IsValid = request.PAY_IsValid

        ret : Pay_Res = await self.DbContext.GetItem[Pay_Res](eSP.proc_Pay_SetPay, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException("수납 저장에 실패했습니다.")
        
        return DataResponse[Pay_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)
