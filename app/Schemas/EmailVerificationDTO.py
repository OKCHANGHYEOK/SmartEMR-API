from app.Schemas.BaseDTO import BaseDTO
from typing import Optional
from decimal import Decimal

class EmailVerificationDTO(BaseDTO):
    EV_Idx : Optional[int] = None
    EV_Purpose : Optional[str] = None
    EV_Email : Optional[str] = None
    EV_CodeOrigin : Optional[str] = None
    EV_CodeHash : Optional[str] = None
    EV_CreatedAt : Optional[str] = None
    EV_ExpiredAt : Optional[str] = None
    EV_AttemptCount : Optional[int] = None
    EV_IsVerified : Optional[bool] = None
    EV_IsValid : Optional[bool] = None

class EmailVerification_Req(EmailVerificationDTO):
    MUR_Name : Optional[str] = None
    MUR_Id : Optional[str] = None

class EmailVerification_Res(EmailVerificationDTO):
    pass
