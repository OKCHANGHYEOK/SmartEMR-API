from .BaseDTO import BaseDTO
from typing import Optional

class InsuranceDTO(BaseDTO):
    IRC_Idx : Optional[int] = None
    MEM_Idx : Optional[int] = None
    PAT_Idx : Optional[int] = None
    RCP_Idx : Optional[int] = None
    IRC_Type : Optional[str] = None
    IRC_CertNum : Optional[str] = None
    IRC_ContractorName : Optional[str] = None
    IRC_InsuredName : Optional[str] = None
    IRC_CoName : Optional[str] = None
    IRC_EffectiveYYMMDD : Optional[str] = None
    IRC_ExpiredYYMMDDD : Optional[str] = None
    IRC_IsValid : Optional[bool] = None

class Insurance_Req(InsuranceDTO):
    pass

class Insurance_Res(InsuranceDTO):
    pass