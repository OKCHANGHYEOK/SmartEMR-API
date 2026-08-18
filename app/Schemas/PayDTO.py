from app.Schemas.BaseDTO import BaseDTO
from typing import Optional
from decimal import Decimal

class PayDTO(BaseDTO):
    PAY_Idx : Optional[int] = None
    MEM_Idx : Optional[int] = None
    MUR_Idx : Optional[int] = None
    PAT_Idx : Optional[int] = None
    CST_Idx : Optional[int] = None
    PAY_Status : Optional[str] = None
    PAY_TotalPrice : Optional[Decimal] = None
    PAY_InsuredPrice : Optional[Decimal] = None
    PAY_NonInsurecPrice : Optional[Decimal] = None
    PAY_OwnPatientPrice : Optional[Decimal] = None
    PAY_PaidPrice : Optional[Decimal] = None
    PAY_RemainPrice : Optional[Decimal] = None
    PAY_Memo : Optional[str] = None
    PAY_Date : Optional[str] = None
    PAY_YYMMDD : Optional[str] = None
    PAY_IsValid : Optional[bool] = None

class Pay_Req(PayDTO):
    pass

class Pay_Res(PayDTO):
    pass

