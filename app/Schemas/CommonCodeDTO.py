from .BaseDTO import BaseDTO
from typing import Optional

class CommonCodeDTO(BaseDTO):
    CCC_Idx : Optional[int] = None
    CCG_Idx : Optional[int] = None
    CCI_Idx : Optional[int] = None
    CCC_Cd : Optional[str] = None
    CCC_Name : Optional[str] = None
    CCG_Cd : Optional[str] = None
    CCG_Name : Optional[str] = None
    CCI_Cd : Optional[str] = None
    CCI_Name : Optional[str] = None

class CommonCode_Req(CommonCodeDTO):
    pass

class CommonCode_Res(CommonCodeDTO):
    pass