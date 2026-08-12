from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from Exceptions.ApiException import ApiException
from Common import eSP
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Services.Domain import BaseService
from Entities.Patient import Patient
from Entities.Reception import Reception
from Entities.Insurance import Insurance
from Entities.Consultation import Consultation
from Schemas.DataResponse import DataResponse
from Schemas.PatientDTO import Patient_Res
from Schemas.ReceptionDTO import Reception_Req, Reception_Res
from Schemas.InsuranceDTO import Insurance_Req, Insurance_Res
from Schemas.ConsultationDTO import Consultation_Req, Consultation_Res
from Factory.InsuranceFactory import InsuranceFactory

class ConsultationService(BaseService):
    def __init__(self, _authenicatedUserSerivce : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserSerivce

    async def GetConsultation(self, request : Consultation_Req) -> DataResponse[Consultation_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : Consultation = Consultation()
        item.MEM_Idx = user.MEM_Idx

        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.PAT_Idx = request.PAT_Idx
        item.RCP_Idx = request.RCP_Idx

        item.CST_Status = request.CST_Status
        item.CST_PayStatus = request.CST_PayStatus
        item.CST_TreatResult = request.CST_TreatResult
        item.CST_Subject = request.CST_Subject
        item.CST_YYMMDD = request.CST_YYMMDD

        item.sDay = request.sDay
        item.eDay = request.eDay
        item.Keyword = request.Keyword
        item.SortField = request.SortField
        item.SortDir = request.SortDir
        item.PageIndex = request.PageIndex
        item.PageSize = request.PageSize

        ret : list[Consultation_Res] = await self.DbContext.GetItems[Consultation_Res](eSP.proc_Consultation_GetConsultation, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException("진료 조회에 실패했습니다.")

        return DataResponse[Consultation_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)

    # 외부에서(예 : ReceptionService) 호출 시 세션이 공유될 수 있도록 매개변수로 선언
    async def SetConsultation(self, request : Consultation_Req, session : AsyncSession | None = None) -> DataResponse[Consultation_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        # 환자가 유효한지 체크
        retPAT : Patient_Res = await self.DbContext.GetItem[Patient_Res](eSP.proc_Patient_GetPatient, Patient(PAT_Idx=request.PAT_Idx), session)

        if not retPAT or self.DbContext.retIsSuccess == False:
            raise ApiException("환자 정보가 유효하지 않습니다.")

        # 접수가 유효한지 체크
        retRCP : Reception_Res = await self.DbContext.GetItem[Reception_Res](eSP.proc_Reception_GetReception, Reception(PAT_Idx=request.PAT_Idx, RCP_Idx=request.RCP_Idx), session)

        if not retRCP or self.DbContext.retIsSuccess == False:
            raise ApiException("접수 정보가 유효하지 않습니다.")

        item : Consultation = Consultation()
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.CST_Idx = request.CST_Idx
        item.PAT_Idx = request.PAT_Idx
        item.RCP_Idx = request.RCP_Idx
        item.MUR_Idx_DOC = request.MUR_Idx_DOC

        item.PAT_ChartNo = retPAT.PAT_ChartNo
        item.PAT_Name = retPAT.PAT_Name
        item.PAT_Sex = retPAT.PAT_Sex
        item.PAT_Age = retPAT.PAT_Age

        item.CST_InsuranceType = request.CST_InsuranceType
        item.CST_Status = request.CST_Status
        item.CST_PayStatus = request.CST_PayStatus
        item.CST_TreatResult = request.CST_TreatResult
        item.CST_Subject = request.CST_Subject
        item.CST_SubjectName = request.CST_SubjectName
        item.CST_StartTime = request.CST_StartTime
        item.CST_EndTime = request.CST_EndTime
        item.CST_Opinion = request.CST_Opinion
        item.CST_Memo = request.CST_Memo
                
        retCST : Consultation_Res = await self.DbContext.GetItem[Consultation_Res](eSP.proc_Consultation_SetConsultation, item, session)

        if not retCST or self.DbContext.retIsSuccess == False:
            raise ApiException("진료 저장하는데 실패했습니다.")

        # 진료 저장 후 보험 정보 저장
        # 기준 보험
        source_insurance : Insurance_Res = None

        # 진료 생성시 -> 접수 보험 / 생성 이후에는 진료의 보험
        isNewCST = True if not request.CST_Idx or request.CST_Idx == 0 else False

        if isNewCST:
            source_insurance = retRCP.IRCItem
        else:
            source_insurance = request.IRCItem

        # 진료가 존재하고 비보험으로 변경된 경우 기존 보험 삭제
        if not isNewCST and source_insurance.IRC_Type == "NON":
            setIRC : Insurance = Insurance()
            setIRC.IRC_Idx = source_insurance.IRC_Idx
            setIRC.IRC_IsValid = False

            await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_SetInsurance, setIRC, session)

            if self.DbContext.retIsSuccess == False:
                raise ApiException("진료보험 삭제에 실패했습니다.")

        else:
            setIRC : Insurance = InsuranceFactory.create(Insurance_Req(source_insurance))
            retIRC : Insurance_Res = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_SetInsurance, setIRC, session)

            if not retIRC or self.DbContext.retIsSuccess == False:
                raise ApiException("진료보험 저장에 실패했습니다.")

            retCST.IRCItem = retIRC

        return DataResponse[Consultation_Res].CreateJsonResult(item=retCST, message=self.DbContext.retMessage)    