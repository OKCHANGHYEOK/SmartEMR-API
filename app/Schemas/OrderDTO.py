from .BaseDTO import BaseDTO
from typing import Optional
from datetime import datetime

class OrderDTO(BaseDTO):
    ORD_Idx : Optional[int] = None
    SUGA_Idx : Optional[int] = None
    ORDC_Cd : Optional[str] = None
    ORDG_Cd : Optional[str] = None
    ORDI_Cd : Optional[str] = None
    ORD_SugaCode : Optional[str] = None
    ORD_ClassCode : Optional[str] = None
    ORD_Name : Optional[str] = None
    ORD_InsuranceType : Optional[str] = None
    ORD_SurgeryType : Optional[str] = None
    ORD_Price : Optional[int] = None
    ORD_Source : Optional[str] = None
    ORD_EffectiveFromDay : Optional[datetime] = None
    ORD_EffectiveToDay : Optional[datetime] = None
    ORD_IsUse : Optional[bool] = None

class Order_Req(OrderDTO):
    pass

class Order_Res(OrderDTO):
    pass