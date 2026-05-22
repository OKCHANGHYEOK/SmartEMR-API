from fastapi import Depends
from Exceptions.ApiException import ApiException
from Entities.Patient import Patient
from Services.Domain import BaseSerivce
from Schemas.DataResponse import DataResponse
from Schemas.PatientDTO import Patient_Req, Patient_Res
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Common import eSP

class PatientService(BaseSerivce):
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
        item.keyword = request.keyword
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        item.SortField = request.SortField
        item.SortDir = request.SortDir

        ret = await self.DbContext.GetItems(eSP.proc_Patient_GetPatient, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Patient_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)