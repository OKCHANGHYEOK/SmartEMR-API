from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.Exceptions.ApiException import ApiException
from app.Common import eSP
from app.Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from app.Services.Domain.BaseService import BaseService
from app.Entities.Patient import Patient
from app.Entities.Reception import Reception
from app.Entities.Insurance import Insurance
from app.Entities.Consultation import Consultation
from app.Entities.ConsultationOrder import ConsultationOrder
from app.Schemas.DataResponse import DataResponse
from app.Schemas.PatientDTO import Patient_Res
from app.Schemas.ReceptionDTO import Reception_Res
from app.Schemas.InsuranceDTO import Insurance_Res
from app.Schemas.ConsultationDTO import Consultation_Req, Consultation_Res
from app.Schemas.ConsultationOrderDTO import ConsultationOrder_Req, ConsultationOrder_Res
from app.Factory.InsuranceFactory import InsuranceFactory

class ConsultationService(BaseService):
    def __init__(self, _authenicatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserService

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

    async def GetConsultationByRCP(self, request : Consultation_Req) -> DataResponse[Consultation_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : Consultation = Consultation()
        item.MEM_Idx = user.MEM_Idx

        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.PAT_Idx = request.PAT_Idx

        item.CST_InsuranceType = request.CST_InsuranceType
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

        ret : list[Consultation_Res] = await self.DbContext.GetItems[Consultation_Res](eSP.proc_Consultation_GetConsultationByRCP, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException("진료 조회에 실패했습니다.")

        return DataResponse[Consultation_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)

    async def SetConsultation(self, request : Consultation_Req) -> DataResponse[Consultation_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        # 환자가 유효한지 체크
        retPAT : Patient_Res = await self.DbContext.GetItem[Patient_Res](eSP.proc_Patient_GetPatient, Patient(PAT_Idx=request.PAT_Idx), session)

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

        item.CST_VisitType = request.CST_VisitType
        item.CST_Status = request.CST_Status
        item.CST_PayStatus = request.CST_PayStatus
        item.CST_TreatResult = request.CST_TreatResult
        item.CST_Subject = request.CST_Subject
        item.CST_SubjectName = request.CST_SubjectName
        item.CST_StartTime = request.CST_StartTime
        item.CST_EndTime = request.CST_EndTime
        item.CST_Opinion = request.CST_Opinion
        item.CST_Memo = request.CST_Memo
        item.CST_IsValid = request.CST_IsValid
                
        retCST : Consultation_Res = await self.DbContext.GetItem[Consultation_Res](eSP.proc_Consultation_SetConsultation, item)

        if not retCST or self.DbContext.retIsSuccess == False:
            raise ApiException("진료 저장하는데 실패했습니다.")

        return DataResponse[Consultation_Res](item=retCST, Message=self.DbContext.retMessage)

    # 외부에서(예 : ReceptionService) 호출 시 세션이 공유될 수 있도록 매개변수로 선언
    async def SetConsultationByCST(self, request : Consultation_Req, session : AsyncSession | None = None) -> DataResponse[Consultation_Res]:
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

        retCST : Consultation_Res = None
        retIRC : Insurance_Res = None

        # 기존 진료 및 보험 조회
        if request.CST_Idx and request.CST_Idx > 0:
            retCST = await self.DbContext.GetItem[Consultation_Res](eSP.proc_Consultation_GetConsultation, Consultation(CST_Idx = request.CST_Idx))

            if not retCST or self.DbContext.retIsSuccess == False:
                raise ApiException("삭제되었거나 존재하지 않는 진료입니다.")

            retIRC = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_GetInsurance, Insurance(IRC_Idx = retCST.IRC_Idx))    

        else:
            retIRC = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_GetInsurance, Insurance(IRC_Idx = retRCP.IRC_Idx))

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

        item.CST_VisitType = request.CST_VisitType
        item.CST_Status = request.CST_Status
        item.CST_PayStatus = request.CST_PayStatus
        item.CST_TreatResult = request.CST_TreatResult
        item.CST_Subject = request.CST_Subject
        item.CST_SubjectName = request.CST_SubjectName
        item.CST_StartTime = request.CST_StartTime
        item.CST_EndTime = request.CST_EndTime
        item.CST_Opinion = request.CST_Opinion
        item.CST_Memo = request.CST_Memo
        item.CST_IsValid = request.CST_IsValid
                
        retCST : Consultation_Res = await self.DbContext.GetItem[Consultation_Res](eSP.proc_Consultation_SetConsultation, item, session)

        if not retCST or self.DbContext.retIsSuccess == False:
            raise ApiException("진료 저장하는데 실패했습니다.")

        # 진료 저장 후 보험 정보 저장
        # 기준 보험
        isNewCST = True if not request.CST_Idx or request.CST_Idx == 0 else False
        source_insurance : Insurance_Res = retIRC if isNewCST else request.IRCItem 

        # 신규 진료 생성 or 보험 변경된 경우 보험 업데이트
        if isNewCST or retIRC.IRC_Type != request.IRCItem.IRC_Type:
            # 비보험이 아닐 때만 보험 저장
            if source_insurance.IRC_Type != "NON":
                setIRC : Insurance = InsuranceFactory.create(source_insurance)
                setIRC.IRC_Idx = 0 if isNewCST else retCST.IRC_Idx

                retIRC : Insurance_Res = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_SetInsurance, setIRC, session)

                if not retIRC or self.DbContext.retIsSuccess == False:
                    raise ApiException("진료보험 저장에 실패했습니다.")    

            # 비보험으로 변경된 경우 보험 데이터가 있다면 해당 보험 데이터 삭제
            elif retCST.IRC_Idx:
                setIRC : Insurance = Insurance()
                setIRC.IRC_Idx = source_insurance.IRC_Idx
                setIRC.IRC_IsValid = False

                retIRC = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_SetInsurance, setIRC, session)

                if self.DbContext.retIsSuccess == False:
                    raise ApiException("진료보험 삭제에 실패했습니다.")

            # 진료 보험 데이터 갱신
            setCSTByIRC = Consultation()    
            setCSTByIRC.MUR_Idx = user.MUR_Idx
            setCSTByIRC.CST_Idx = retCST.CST_Idx
            setCSTByIRC.IRC_Idx = retIRC.IRC_Idx
            setCSTByIRC.CST_InsuranceType = retIRC.IRC_Type

            retCST = await self.DbContext.GetItem[Consultation_Res](eSP.proc_Consultation_SetConsultationByIRC, setCSTByIRC)

            if not retCST or self.DbContext.retIsSuccess == False:
                raise ApiException("보험 정보 업데이트에 실패했습니다")

            retCST.IRCItem = retIRC    

        # 오더 저장
        if request.CSTO_Property:
            setCSTO = ConsultationOrder()
            setCSTO.MEM_Idx = user.MEM_Idx  
            setCSTO.MUR_Idx = user.MUR_Idx
            setCSTO.CST_Idx = retCST.CST_Idx
            setCSTO.PAT_Idx = retPAT.PAT_Idx
            setCSTO.CSTO_Property = request.CSTO_Property

            await self.DbContext.GetItems[ConsultationOrder_Req](eSP.proc_ConsultationOrder_SetConsultationOrderProperty, setCSTO)

            if self.DbContext.retIsSuccess == False:
                raise ApiException("처방 저장에 실패했습니다.")
            
        return DataResponse[Consultation_Res].CreateJsonResult(item=retCST, message=self.DbContext.retMessage)    