from fastapi import Depends
from Exceptions.ApiException import ApiException
from Entities.Reception import Reception
from Services.Domain import BaseService
from Schemas.DataResponse import DataResponse
from Schemas.ReceptionDTO import Reception_Req, Reception_Res
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Services.Authentication.CryptoService import CryptoService
from Common import eSP

class ReceptionService(BaseService):
    def __init__(self, _authenicatedUserSerivce : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserSerivce

    async def GetReception(self, request: Reception_Req):
        item : Reception = Reception()

        user = self.authenticatedUserService.GetUser()

        if user == None:
            return
        
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.PAT_Idx = request.PAT_Idx

        item.RCP_Status = request.RCP_Status
        item.RCP_Route = request.RCP_Route

        item.Keyword = request.Keyword
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        item.SortField = request.SortField
        item.SortDir = request.SortDir

        ret = await self.DbContext.GetItems(eSP.proc_Reception_GetReception, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Reception_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)
    
    async def SetReception(self, request: Reception_Req):
        item : Reception = Reception()

        user = self.authenticatedUserService.GetUser()

        if user == None:
            return
        
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.PAT_Idx = request.PAT_Idx
        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.MUR_Idx_STF = request.MUR_Idx_STF
        item.PAT_Name = request.PAT_Name
        item.PAT_ChartNo = request.PAT_ChartNo
        item.PAT_Sex = request.PAT_Sex
        item.PAT_Age = request.PAT_Age
        item.RCP_Status = request.RCP_Status
        item.RCP_Route = request.RCP_Route
        item.RCP_Subject = request.RCP_Subject
        item.RCP_InsuranceType = request.RCP_InsuranceType
        item.RCP_ReceiptDate = request.RCP_ReceiptDate
        item.RCP_ReceiptTime = request.RCP_ReceiptTime
        item.RCP_StartTreatTime = request.RCP_StartTreatTime
        item.RCP_EndTreatTime = request.RCP_EndTreatTime
        item.RCP_Memo = request.RCP_Memo
        item.RCP_IsValid = request.RCP_IsValid

        ret = await self.DbContext.GetItems(eSP.proc_Reception_SetReception, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Reception_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)