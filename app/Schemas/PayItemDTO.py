from app.Schemas.BaseDTO import BaseDTO
from typing import Optional
from decimal import Decimal

class PayItemDTO(BaseDTO):
    PAYI_Idx : Optional[int] = None
    PAY_Idx : Optional[int] = None
    MEM_Idx : Optional[int] = None
    MUR_Idx : Optional[int] = None
    PAT_Idx : Optional[int] = None
    PAYI_Type : Optional[str] = None
    PAYI_Method : Optional[str] = None
    PAYI_Price : Optional[Decimal] = None
    PAYI_Time : Optional[str] = None
    PAYI_Date : Optional[str] = None
    PAYI_YYMMDD : Optional[str] = None
    PAYI_IsValid : Optional[bool] = None


class PayItem_Req(PayItemDTO):
    pass

class PayItem_Res(PayItemDTO):
    MUR_Name : Optional[str] = None