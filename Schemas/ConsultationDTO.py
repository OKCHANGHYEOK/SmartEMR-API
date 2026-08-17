from .BaseDTO import BaseDTO
from typing import Optional
from decimal import Decimal
from Schemas.InsuranceDTO import Insurance_Req, Insurance_Res

class ConsultationDTO(BaseDTO):
    CST_Idx : Optional[int] = None
    MEM_Idx : Optional[int] = None
    MUR_Idx : Optional[int] = None
    MUR_Idx_DOC : Optional[int] = None
    PAT_Idx : Optional[int] = None
    RCP_Idx : Optional[int] = None
    IRC_Idx : Optional[int] = None
    CST_InsuranceType : Optional[str] = None
    CST_Status : Optional[str] = None
    CST_PayStatus : Optional[str] = None
    CST_TreatResult : Optional[str] = None
    CST_Subject : Optional[str] = None
    CST_SubjectName : Optional[str] = None
    CST_StartTime : Optional[str] = None
    CST_EndTime : Optional[str] = None
    CST_TotalPrice : Optional[Decimal] = None
    CST_InsuredPrice : Optional[Decimal] = None
    CST_NonInsurecPrice : Optional[Decimal] = None
    CST_OwnPatientPrice : Optional[Decimal] = None
    CST_PaidPrice : Optional[Decimal] = None
    CST_RemainPrice : Optional[Decimal] = None
    CST_Opinion : Optional[str] = None
    CST_Memo : Optional[str] = None
    CST_Date : Optional[str] = None
    CST_YYMMDD : Optional[str] = None
    CST_IsValid : Optional[bool] = None

    IRCItem : Insurance_Res = None

    sDay : Optional[str] = None
    eDay : Optional[str] = None

class Consultation_Req(ConsultationDTO):
    pass

class Consultation_Res(ConsultationDTO):
    MUR_Name_DOC : Optional[str] = None

    PAT_Name: Optional[str] = None
    PAT_ChartNo: Optional[str] = None
    PAT_Sex: Optional[str] = None
    PAT_Age: Optional[int] = None

