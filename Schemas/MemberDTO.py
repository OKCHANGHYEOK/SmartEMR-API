from .BaseDTO import BaseDTO
from typing import Optional

class MemberDTO(BaseDTO):
    MEM_Idx : Optional[int] = None
    MEM_Name : Optional[str] = None
    MEM_MediNo : Optional[str] = None
    MEM_BizNum : Optional[str] = None
    MEM_BizType : Optional[str] = None
    MEM_Address1 : Optional[str] = None
    MEM_Address2 : Optional[str] = None
    MEM_Address3 : Optional[str] = None
    MEM_Tel1 : Optional[str] = None
    MEM_Tel2 : Optional[str] = None
    MEM_Tel3 : Optional[str] = None
    MEM_StartDate : Optional[str] = None
    MEM_EndDate : Optional[str] = None
    MEM_OperationStatus : Optional[int] = None
    MEM_AdminUser : Optional[int] = None
    MEM_Date : Optional[str] = None
    MEM_YYMMDD : Optional[str] = None
    MEM_IsValid : Optional[bool] = None

class Member_Req(MemberDTO):
    MUR_Idx : Optional[int] = None

class Member_Res(MemberDTO):
    MEM_AdminUserName : Optional[str] = None        