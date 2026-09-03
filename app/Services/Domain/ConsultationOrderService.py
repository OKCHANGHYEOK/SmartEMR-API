from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.Exceptions.ApiException import ApiException
from app.Common import eSP
from app.Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from app.Services.Domain.BaseService import BaseService
from app.Entities.ConsultationOrder import ConsultationOrder
from app.Schemas.DataResponse import DataResponse
from app.Schemas.ConsultationOrderDTO import ConsultationOrder_Req, ConsultationOrder_Res

class ConsultationOrderService(BaseService):
    def __init__(self, _authenicatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserService

    async def GetConsultationOrder(self, request : ConsultationOrder_Req) -> DataResponse[ConsultationOrder_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : ConsultationOrder = ConsultationOrder()
        item.MEM_Idx = user.MEM_Idx

        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.PAT_Idx = request.PAT_Idx
        item.CST_Idx = request.CST_Idx

        item.CSTO_Status = request.CSTO_Status
        item.CSTO_InsuranceType = request.CSTO_InsuranceType

        item.sDay = request.sDay
        item.eDay = request.eDay
        item.Keyword = request.Keyword
        item.SortField = request.SortField
        item.SortDir = request.SortDir
        item.PageIndex = request.PageIndex
        item.PageSize = request.PageSize

        ret : list[ConsultationOrder_Res] = await self.DbContext.GetItems[ConsultationOrder_Res](eSP.proc_ConsultationOrder_GetConsultationOrder, item)

        if self.DbContext.retIsSuccess == False:
            raise ApiException("처방 조회에 실패했습니다.")

        return DataResponse[ConsultationOrder_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)

    async def SetConsultationOrder(self, request : ConsultationOrder_Req) -> DataResponse[ConsultationOrder_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : ConsultationOrder = ConsultationOrder()
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.PAT_Idx = request.PAT_Idx
        item.CST_Idx = request.CST_Idx
        item.ORD_Idx = request.ORD_Idx

        item.ORDC_Cd = request.ORDC_Cd
        item.ORDG_Cd = request.ORDG_Cd
        item.ORDI_Cd = request.ORDI_Cd

        item.CSTO_SugaCode = request.CSTO_SugaCode
        item.CSTO_ClassCode = request.CSTO_ClassCode
        item.CSTO_InsuranceType = request.CSTO_InsuranceType
        item.CSTO_Status = request.CSTO_Status
        item.CSTO_Name = request.CSTO_Name
        item.CSTO_Day = request.CSTO_Day
        item.CSTO_Count = request.CSTO_Count
        item.CSTO_Amount = request.CSTO_Amount
        item.CSTO_TotalPrice = request.CSTO_TotalPrice
        item.CSTO_Memo = request.CSTO_Memo
        item.CSTO_IsValid = request.CSTO_IsValid

        ret : ConsultationOrder_Res = await self.DbContext.GetItem[ConsultationOrder_Res](eSP.proc_ConsultationOrder_SetConsultationOrder, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException("처방 저장에 실패했습니다.")

        return DataResponse[ConsultationOrder_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)