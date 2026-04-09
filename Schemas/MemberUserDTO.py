from .BaseDTO import BaseDTO
from typing import Optional

class MemberUserDTO(BaseDTO):
    MUR_Idx : Optional[int] = None
    MEM_Idx : Optional[int] = None
    MUR_Id : Optional[str] = None
    MUR_PassWord : Optional[str] = None
    MUR_Name : Optional[str] = None
    MUR_Role : Optional[str] = None
    MUR_JobCode : Optional[str] = None
    MUR_Gender : Optional[str] = None
    MUR_Address1 : Optional[str] = None
    MUR_Address2 : Optional[str] = None
    MUR_Address3 : Optional[str] = None
    MUR_Age : Optional[int] = None
    MUR_BirthYear : Optional[str] = None
    MUR_BirthMonth : Optional[str] = None
    MUR_BirthDay : Optional[str] = None
    MUR_PhoneNum1 : Optional[str] = None
    MUR_PhoneNum2 : Optional[str] = None
    MUR_PhoneNum3 : Optional[str] = None
    MUR_Email : Optional[str] = None
    MUR_Date : Optional[str] = None
    MUR_YYMMDD : Optional[str] = None
    MUR_IsValid : Optional[bool] = None

class MemberUser_Req(MemberUserDTO):
    pass

class MemberUser_Res(MemberUserDTO):
    MUR_Idx_DOC : Optional[int] = None
    MUR_Name_DOC : Optional[str] = None
    MUR_Idx_STF : Optional[str] = None
    MUR_Name_STF : Optional[str] = None
