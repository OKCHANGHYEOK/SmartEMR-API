from fastapi import Depends
from Exceptions.ApiException import ApiException
from Entities.Patient import Patient
from Entities.Reservation import Reservation
from Services.Domain import BaseService
from Schemas.DataResponse import DataResponse
from Schemas.PatientDTO import Patient_Res
from Schemas.ReservationDTO import Reservation_Req, Reservation_Res
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Services.Domain.PatientService import PatientService
from Common import eSP

class ReservationService(BaseService):
    def __init__(self, 
                 _authenicatedUserSerivce : AuthenticatedUserService = Depends(AuthenticatedUserService),
                 _patientService : PatientService = Depends(PatientService)):
        self.authenticatedUserService = _authenicatedUserSerivce
        self.patientService = _patientService

    async def GetReservation(self, request : Reservation_Req) -> DataResponse[Reservation_Res]:
        item : Reservation = Reservation()

        user = self.authenticatedUserService.GetUser()

        if user == None:
            raise ApiException("유저가 올바르지 않습니다.")
        
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.PAT_Idx = request.PAT_Idx

        item.RES_Idx = request.RES_Idx
        item.RES_Status = request.RES_Status
        item.RES_Route = request.RES_Route
        item.RES_Subject = request.RES_Subject
        item.RES_YYMMDD = request.RES_YYMMDD

        item.Keyword = request.Keyword
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        item.SortField = request.SortField
        item.SortDir = request.SortDir

        ret = await self.DbContext.GetItems[Reservation_Res](eSP.proc_Reservation_GetReservation, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Reservation_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)
    
    async def SetReservation(self, request : Reservation_Req) -> DataResponse[Reservation_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        # 신환예약인 경우 환자생성, 기존 환자예약인 경우 환자조회
        patient : Patient = request.PATItem
        retPAT : Patient_Res = None

        if patient.PAT_Idx == 0:
            setPAT = await self.patientService.SetPatient(patient)

            if setPAT:
                retPAT = setPAT.Item
        else:
            retPAT = await self.DbContext.GetItem[Patient_Res](eSP.proc_Patient_GetPatient, Patient( PAT_Idx = patient.PAT_Idx ))

        if retPAT is None or self.DbContext.retIsSuccess == False:
            raise ApiException(f"환자 {'저장' if patient else '조회'}에 실패햇습니다.")   
        
        item : Reservation = Reservation()

        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.MUR_Idx_STF = request.MUR_Idx_STF

        item.PAT_Idx = retPAT.PAT_Idx
        item.PAT_Name = retPAT.PAT_Name
        item.PAT_ChartNo = retPAT.PAT_ChartNo
        item.PAT_Sex = retPAT.PAT_Sex
        item.PAT_Age = retPAT.PAT_Age

        item.RES_Idx = request.RES_Idx
        item.RES_Status = request.RES_Status
        item.RES_Route = request.RES_Route
        item.RES_Subject = request.RES_Subject
        item.RES_SubjectName = request.RES_SubjectName
        item.RES_ReservationDate = request.RES_ReservationDate
        item.RES_ReservationTime = request.RES_ReservationTime
        item.RES_Memo = request.RES_Memo
        item.RES_IsValid = request.RES_IsValid

        ret : Reservation_Res = await self.DbContext.GetItem[Reservation_Res](eSP.proc_Reservation_SetReservation, item)

        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Reservation_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)