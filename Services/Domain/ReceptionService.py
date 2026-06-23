from fastapi import Depends
from Exceptions.ApiException import ApiException
from Entities.Patient import Patient
from Entities.Reception import Reception
from Entities.Insurance import Insurance
from Services.Domain import BaseService
from Schemas.DataResponse import DataResponse
from Schemas.ReceptionDTO import Reception_Req, Reception_Res
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
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
        item.RCP_YYMMDD = request.RCP_YYMMDD

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

        retPAT = await self.DbContext.GetItem(eSP.proc_Patient_GetPatient, Patient( PAT_Idx = request.PAT_Idx ))

        if retPAT is None or self.DbContext.retIsSuccess == False:
            raise ApiException("환자 조회에 실패햇습니다.")
        
        item.PAT_Name = retPAT.PAT_Name
        item.PAT_ChartNo = retPAT.PAT_ChartNo
        item.PAT_Sex = retPAT.PAT_Sex
        item.PAT_Age = retPAT.PAT_Age

        item.RCP_Idx = request.RCP_Idx
        item.RCP_Status = request.RCP_Status
        item.RCP_Route = request.RCP_Route
        item.RCP_VisitType = request.RCP_VisitType
        item.RCP_Subject = request.RCP_Subject3EndTreatTime
        item.RCP_Memo = request.RCP_Memo
        item.RCP_IsValid = request.RCP_IsValid

        ret = await self.DbContext.GetItems(eSP.proc_Reception_SetReception, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        RCPItem = ret[0]

        if request.IRCItem:
            IRCItem = request.IRCItem

            setIRC : Insurance = Insurance()

            # 비보험일 때 이미 해당 접수의 보험이 있으면 삭제 처리
            if IRCItem.IRC_Idx > 0 and IRCItem.IRC_Type == "NOR":
                setIRC.IRC_Idx = IRCItem.IRC_Idx
                setIRC.IRC_IsValid = False

                await self.DbContext.GetItem(eSP.proc_Insurance_SetInsurance, setIRC)

            else:
                setIRC.MEM_Idx = user.MEM_Idx
                setIRC.IRC_Idx = IRCItem.IRC_Idx
                setIRC.RCP_Idx = RCPItem.RCP_Idx
                setIRC.PAT_Idx = RCPItem.PAT_Idx
                setIRC.IRC_Type = IRCItem.IRC_Type
                setIRC.IRC_CertNum = IRCItem.IRC_CertNum
                setIRC.IRC_ContractorName = IRCItem.IRC_ContractorName
                setIRC.IRC_InsuredName = IRCItem.IRC_InsuredName
                setIRC.IRC_CoName = IRCItem.IRC_CoName
                setIRC.IRC_EffectiveYYMMDD = IRCItem.IRC_EffectiveYYMMDD
                setIRC.IRC_ExpiredYYMMDD = IRCItem.IRC_ExpiredYYMMDDD

                retIRC = await self.DbContext.GetItem(eSP.proc_Insurance_SetInsurance, setIRC)

                if retIRC is None or self.DbContext.retIsSuccess == False:
                    raise ApiException(self.DbContext.retMessage)

        return DataResponse[Reception_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)