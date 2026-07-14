from .BaseDTO import BaseDTO
from typing import Optional
from decimal import Decimal

class ConsultationDTO(BaseDTO):
    CST_Idx : Optional[int] = None
    MEM_Idx : Optional[int] = None
    MUR_Idx : Optional[int] = None
    PAT_Idx : Optional[int] = None
    RCP_Idx : Optional[int] = None
    CST_Status : Optional[str] = None
    CST_PayStatus : Optional[str] = None
    CST_TreatResult : Optional[str] = None
    CST_Subject : Optional[str] = None
    CST_SubjectName : Optional[str] = None
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

class Consultation_Req(ConsultationDTO):
    pass

class Consultation_Req(ConsultationDTO):
    pass
