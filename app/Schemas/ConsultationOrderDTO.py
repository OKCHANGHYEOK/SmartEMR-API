from .BaseDTO import BaseDTO
from typing import Optional
from decimal import Decimal

class ConsultationOrderDTO(BaseDTO):
    CSTO_Idx : Optional[int] = None
    MEM_Idx : Optional[int] = None
    MUR_Idx : Optional[int] = None
    MUR_Idx_DOC : Optional[int] = None
    PAT_Idx : Optional[int] = None
    CST_Idx : Optional[int] = None
    ORD_Idx : Optional[int] = None
    ORDC_Cd : Optional[str] = None
    ORDG_Cd : Optional[str] = None
    ORDI_Cd : Optional[str] = None
    CSTO_SugaCode : Optional[str] = None
    CSTO_ClassCode : Optional[str] = None
    CSTO_InsuranceType : Optional[str] = None
    CSTO_Status : Optional[str] = None
    CSTO_Name : Optional[str] = None
    CSTO_Day : Optional[int] = None
    CSTO_Count : Optional[int] = None
    CSTO_Amount : Optional[int] = None
    CSTO_Price : Optional[Decimal] = None
    CSTO_TotalPrice : Optional[Decimal] = None
    CSTO_Memo : Optional[str] = None
    CSTO_Date : Optional[str] = None
    CSTO_YYMMDD : Optional[str] = None
    CSTO_IsValid : Optional[bool] = None

    sDay : Optional[str] = None
    eDay : Optional[str] = None

class ConsultationOrder_Req(ConsultationOrderDTO):
    pass

class ConsultationOrder_Res(ConsultationOrderDTO):
    pass