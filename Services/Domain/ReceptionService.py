from fastapi import Depends
from Exceptions.ApiException import ApiException
from Common import eSP
from datetime import datetime
from Entities.Patient import Patient
from Entities.Reception import Reception
from Entities.Insurance import Insurance
from Services.Domain import BaseService
from Schemas.DataResponse import DataResponse
from Schemas.PatientDTO import Patient_Res
from Schemas.ReceptionDTO import Reception_Req, Reception_Res
from Schemas.ReservationDTO import Reservation_Req, Reservation_Res
from Schemas.ReceptionBoardDTO import ReceptionBoard_Req, ReceptionBoard_Res
from Schemas.InsuranceDTO import Insurance_Req, Insurance_Res
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Factory.InsuranceFactory import InsuranceFactory

class ReceptionService(BaseService):
    def __init__(self, _authenicatedUserSerivce : AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenicatedUserSerivce

    async def GetReception(self, request: Reception_Req) -> DataResponse[Reception_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : Reception = Reception()
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

        ret = await self.DbContext.GetItems[Reception_Res](eSP.proc_Reception_GetReception, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Reception_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)
    
    async def GetReceptionBoard(self, request: ReceptionBoard_Req) -> DataResponse[ReceptionBoard_Res]:
            user = self.authenticatedUserService.GetUser()

            if not user:
                raise ApiException("유저가 올바르지 않습니다.")

            item : ReceptionBoard_Req = ReceptionBoard_Req()
            item.MEM_Idx = user.MEM_Idx
            item.MUR_Idx_DOC = request.MUR_Idx_DOC
            item.PAT_Idx = request.PAT_Idx

            item.RCP_Status = request.RCP_Status
            item.RCP_InsuranceType = request.RCP_InsuranceType

            item.RES_Status = request.RES_Status

            item.RCB_Type = request.RCB_Type
            item.RCB_Route = request.RCB_Route
            item.RCB_Subject = request.RCB_Subject
            item.RCB_VisitType = request.RCB_VisitType
            item.RCB_YYMMDD = request.RCB_YYMMDD

            item.Keyword = request.Keyword
            item.PageSize = request.PageSize
            item.PageIndex = request.PageIndex
            item.SortField = request.SortField
            item.SortDir = request.SortDir

            ret : list[ReceptionBoard_Res] = await self.DbContext.GetItems[ReceptionBoard_Res](eSP.proc_Reception_GetReceptionBoard, item)

            if ret is None or self.DbContext.retIsSuccess == False:
                raise ApiException(self.DbContext.retMessage)
            
            return DataResponse[ReceptionBoard_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)

    async def SetReception(self, request: Reception_Req) -> DataResponse[Reception_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        # 삭제일 때는 미리 처리하고 종료
        if request.RCP_IsValid == False:
            delRCP = Reception()
            delRCP.MEM_Idx = user.MEM_Idx
            delRCP.MUR_Idx = user.MUR_Idx
            delRCP.RCP_Idx = request.RCP_Idx
            delRCP.RCP_IsValid = request.RCP_IsValid

            await self.DbContext.GetItem[Reception_Res](eSP.proc_Reception_CancelReception, delRCP)

            if self.DbContext.retIsSuccess == False:
                raise ApiException("접수 삭제하지 못했습니다.")
            
            return DataResponse[Reception_Res].CreateDefaultResult()

        item : Reception = Reception()
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.PAT_Idx = request.PAT_Idx
        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.MUR_Idx_STF = request.MUR_Idx_STF

        retPAT : Patient_Res = await self.DbContext.GetItem[Patient_Res](eSP.proc_Patient_GetPatient, Patient( PAT_Idx = request.PAT_Idx ))

        if retPAT is None or self.DbContext.retIsSuccess == False:
            raise ApiException("환자 조회에 실패햇습니다.")
        
        item.PAT_Name = retPAT.PAT_Name
        item.PAT_ChartNo = retPAT.PAT_ChartNo
        item.PAT_Sex = retPAT.PAT_Sex
        item.PAT_Age = retPAT.PAT_Age

        item.RCP_Idx = request.RCP_Idx
        item.RES_Idx = request.RES_Idx
        item.RCP_Status = request.RCP_Status
        item.RCP_Route = request.RCP_Route
        item.RCP_VisitType = request.RCP_VisitType
        item.RCP_InsuranceType = request.RCP_InsuranceType
        item.RCP_Subject = request.RCP_Subject
        item.RCP_SubjectName = request.RCP_SubjectName
        item.RCP_ReceiptDate = request.RCP_ReceiptDate
        item.RCP_ReceiptTime = request.RCP_ReceiptTime
        item.RCP_Memo = request.RCP_Memo
        item.RCP_IsValid = request.RCP_IsValid

        async with self.DbContext.AsyncSessionLocal() as session:
            try:
                ret : Reception_Res = None
                isNewRCP = True if not request.RCP_Idx or request.RCP_Idx == 0 else False

                # 접수 등록이고 예약키값이 존재하는 경우
                if isNewRCP and request.RES_Idx > 0:
                    ret = await self.DbContext.GetItem[Reception_Res](eSP.proc_Reception_SetReceptionByRES, item, session)
                # 예약없이 접수 등록 or 접수 등록 이후인 경우
                else:
                    ret = await self.DbContext.GetItem[Reception_Res](eSP.proc_Reception_SetReception, item, session)    

                if ret is None or self.DbContext.retIsSuccess == False:
                    raise ApiException(self.DbContext.retMessage)

                IRCItem = request.IRCItem

                if IRCItem:
                    IRC_Idx = IRCItem.IRC_Idx
                    isNewIRC = True if not IRC_Idx or IRC_Idx == 0 else False

                    setIRC : Insurance = None

                    # 비보험일 때 이미 해당 접수의 보험이 있으면 삭제 처리
                    if not isNewIRC and IRCItem.IRC_Type == "NON":
                        setIRC = Insurance()
                        setIRC.IRC_Idx = IRC_Idx
                        setIRC.IRC_IsValid = False

                        await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_SetInsurance, setIRC, session)

                    else:
                        setIRC = InsuranceFactory.create(IRCItem)
                        setIRC.MEM_Idx = user.MEM_Idx
                        setIRC.IRC_Idx = IRC_Idx
                        setIRC.PAT_Idx = ret.PAT_Idx                        

                        retIRC : Insurance_Res = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_SetInsurance, setIRC, session)

                        if retIRC is None or self.DbContext.retIsSuccess == False:
                            raise ApiException("보험 저장에 실패했습니다.")

                        if isNewIRC:
                            # 보험 저장 이후 접수 보험키값 갱신
                            setRCPByIRC = Reception()
                            setRCPByIRC.RCP_Idx = ret.RCP_Idx
                            setRCPByIRC.IRC_Idx = retIRC.IRC_Idx

                            ret = await self.DbContext.GetItem[Reception_Res](eSP.proc_Reception_SetReceptionByIRC, setRCPByIRC, session)

                            if ret is None or self.DbContext.retIsSuccess == False:
                                raise ApiException("접수 보험 키값을 업데이트 하지 못했습니다.")

                        ret.IRCItem = retIRC

                await session.commit()

            except:
                await session.rollback()
                raise

        return DataResponse[Reception_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)

    async def SetReceptionByRES(self, request : Reservation_Req) -> DataResponse[Reception_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")

        item : Reception = Reception()
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.PAT_Idx = request.PAT_Idx
        item.MUR_Idx_DOC = request.MUR_Idx_DOC
        item.MUR_Idx_STF = request.MUR_Idx_STF

        retPAT : Patient_Res = await self.DbContext.GetItem[Patient_Res](eSP.proc_Patient_GetPatient, Patient( PAT_Idx = request.PAT_Idx ))

        if retPAT is None or self.DbContext.retIsSuccess == False:
            raise ApiException("환자 조회에 실패햇습니다.")

        # 예약 등록시에는 보험 정보가 없으므로, 가장 최근의 보험정보를 가져옴
        getIRC = Insurance()
        getIRC.PAT_Idx = request.PAT_Idx
        getIRC.SortField = "IRC_YYMMDD"
        getIRC.SortDir = "desc"

        retIRC : Insurance_Res = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_GetInsurance, getIRC)

        item.PAT_Name = retPAT.PAT_Name
        item.PAT_ChartNo = retPAT.PAT_ChartNo
        item.PAT_Sex = retPAT.PAT_Sex
        item.PAT_Age = retPAT.PAT_Age

        item.RCP_Idx = 0
        item.RES_Idx = request.RES_Idx
        item.RCP_Status = "RDY"
        item.RCP_Route = request.RES_Route
        item.RCP_VisitType = 'REP' if retIRC else 'FIR'
        item.RCP_InsuranceType = retIRC.IRC_Type if retIRC else 'NON'
        item.RCP_Subject = request.RES_Subject
        item.RCP_SubjectName = request.RES_SubjectName
        item.RCP_ReceiptDate = datetime.today().strftime("%Y-%m-%d")
        item.RCP_ReceiptTime = datetime.now().strftime("%H:%M")
        item.RCP_IsValid = True

        async with self.DbContext.AsyncSessionLocal() as session:
            try:
                ret : Reception_Res = await self.DbContext.GetItem[Reception_Res](eSP.proc_Reception_SetReceptionByRES, item)

                if ret is None or self.DbContext.retIsSuccess == False:
                    raise ApiException(self.DbContext.retMessage)

                if retIRC:
                    setIRC : Insurance = InsuranceFactory.create(Insurance_Req(retIRC))
                    setIRC.IRC_Idx = 0
                    setIRC.PAT_Idx = ret.PAT_Idx
                    setIRC.IRC_Type = retIRC.IRC_Type

                    retIRC : Insurance_Res = await self.DbContext.GetItem[Insurance_Res](eSP.proc_Insurance_SetInsurance, setIRC, session)

                    if retIRC is None or self.DbContext.retIsSuccess == False:
                        raise ApiException("보험 저장에 실패했습니다.")

                    # 보험 저장 이후 접수 보험키값 갱신
                    setRCPByIRC = Reception()
                    setRCPByIRC.RCP_Idx = ret.RCP_Idx
                    setRCPByIRC.IRC_Idx = retIRC.IRC_Idx

                    ret = await self.DbContext.GetItem[Reception_Res](eSP.proc_Reception_SetReceptionByIRC, setRCPByIRC, session)

                    if ret is None or self.DbContext.retIsSuccess == False:
                        raise ApiException("접수 보험 키값을 업데이트 하지 못했습니다.")

                await session.commit()

            except:
                await session.rollback()
                raise    

        return DataResponse[Reception_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)

    async def CancelReception(self, request : Reception_Req) -> DataResponse[Reception_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("환자 조회에 실패햇습니다.")

        item : Reception = Reception()
        item.MEM_Idx = user.MEM_Idx
        item.MUR_Idx = user.MUR_Idx

        item.RCP_Idx = request.RCP_Idx    
        item.RES_Idx = request.RES_Idx

        await self.DbContext.GetItem[Reception_Res](eSP.proc_Reception_CancelReception, item)

        if self.DbContext.retIsSuccess == False:
            raise ApiException("접수취소하지 못했습니다.")

        return DataResponse[Reception_Res].CreateDefaultResult()