from fastapi import Depends
from Exceptions.ApiException import ApiException
from Entities.Patient import Patient
from Services.Domain import BaseService
from Schemas.DataResponse import DataResponse
from Schemas.PatientDTO import Patient_Req, Patient_Res
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Services.Authentication.CryptoService import CryptoService
from Common import eSP
from Common import Common

class PatientService(BaseService):
    def __init__(self, _authenicatedUserSerivce : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserSerivce

    async def GetPatient(self, request: Patient_Req):
        item : Patient = Patient()

        user = self.authenticatedUserService.GetUser()

        if user == None:
            return
        
        item.MEM_Idx = user.MEM_Idx
        item.PAT_Idx = request.PAT_Idx
        item.PAT_Name = request.PAT_Name
        item.PAT_ChartNo = request.PAT_ChartNo
        item.PAT_Sex = request.PAT_Sex
        item.Keyword = request.Keyword
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        item.SortField = request.SortField
        item.SortDir = request.SortDir

        ret = await self.DbContext.GetItems(eSP.proc_Patient_GetPatient, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Patient_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)
    
    async def SetPatient(self, request: Patient_Req):
        item : Patient = Patient()

        user = self.authenticatedUserService.GetUser()

        if user == None:
            return
        
        PAT_Birth = request.PAT_BirthYear + request.PAT_BirthMonth + request.PAT_BirthDay

        if len(PAT_Birth) != 8:
            raise ApiException("생년월일이 올바르지 않습니다.", res_code=400)

        # 차트번혼 설정
        PAT_ChartNo = Common.GenerateChartNo(PAT_Birth)

        if len(PAT_ChartNo) != 20:
            raise ApiException("차트번호 생성에 실패했습니다. 잠시후 다시 시도하세요.", res_code=500)

        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.PAT_Idx = request.PAT_Idx
        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.MUR_Idx_STF = request.MUR_Idx_STF
        item.PAT_ChartNo = PAT_ChartNo
        item.PAT_Sex = request.PAT_Sex
        item.PAT_Age = request.PAT_Age
        item.PAT_BirthDay = request.PAT_BirthYear
        item.PAT_BirthMonth = request.PAT_BirthMonth
        item.PAT_BirthDay = request.PAT_BirthDay
        item.PAT_RegisterNum1 = request.PAT_RegisterNum1
        item.PAT_RegisterNum2 = CryptoService.Encrypt(request.PAT_RegisterNum2)
        item.PAT_Hpp1 = request.PAT_Hpp1
        item.PAT_Hpp2 = request.PAT_Hpp2
        item.PAT_Hpp3 = request.PAT_Hpp3
        item.PAT_Address1 = request.PAT_Address1
        item.PAT_Address2 = request.PAT_Address2
        item.PAT_Address3 = request.PAT_Address3
        item.PAT_Email = request.PAT_Email
        item.PAT_FirstVisitDate = request.PAT_FirstVisitDate
        item.PAT_LastVisitDate = request.PAT_LastVisitDate
        item.PAT_IsSolar = request.PAT_IsSolar
        item.PAT_IsAgreePersonalInfo = request.PAT_IsAgreePersonalInfo
        item.PAT_IsForeign = request.PAT_IsForeign
        item.PAT_IsSMS = request.PAT_IsSMS
        item.PAT_IsEmail = request.PAT_IsEmail
        item.PAT_IsValid = request.PAT_IsValid        

        ret = await self.DbContext.GetItems(eSP.proc_Patient_GetPatient, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Patient_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)