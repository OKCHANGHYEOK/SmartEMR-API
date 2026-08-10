from fastapi import Depends
from Exceptions.ApiException import ApiException
from Entities.Insurance import Insurance
from Services.Domain import BaseService
from Schemas.DataResponse import DataResponse
from Schemas.InsuranceDTO import Insurance_Req, Insurance_Res
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Common import eSP

class InsuranceService(BaseService):
    def __init__(self, _authenicatedUserSerivce : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserSerivce

    async def GetInsurance(self, request: Insurance_Req) -> DataResponse[Insurance_Res]:
        item : Insurance = Insurance()

        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")
        
        item.MEM_Idx = user.MEM_Idx

        item.IRC_Idx = request.IRC_Idx
        item.PAT_Idx = request.PAT_Idx
        item.IRC_Type = request.IRC_Type

        item.Keyword = request.Keyword
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        item.SortField = request.SortField
        item.SortDir = request.SortDir

        ret = await self.DbContext.GetItems[Insurance_Res](eSP.proc_Insurance_GetInsurance, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Insurance_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)

    async def SetInsurance(self, request : Insurance_Req) -> DataResponse[Insurance_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : Insurance = Insurance()

        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.IRC_Idx = request.IRC_Idx
        item.PAT_Idx = request.PAT_Idx
        item.RCP_Idx = request.RCP_Idx
        item.CST_Idx = request.CST_Idx

        item.IRC_Type = request.IRC_Type
        item.IRC_CertNum = request.IRC_CertNum
        item.IRC_ContractorName = request.IRC_ContractorName
        item.IRC_InsuredName = request.IRC_InsuredName
        item.IRC_CoName = request.IRC_CoName
        item.IRC_Specific = request.IRC_Specific
        item.IRC_EffectiveYYMMDD = request.IRC_EffectiveYYMMDD
        item.IRC_ExpiredYYMMDD = request.IRC_ExpiredYYMMDDD    

        ret : Insurance_Res = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_SetInsurance, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException("보험 저장에 실패했습니다.")

        return DataResponse[Insurance_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)