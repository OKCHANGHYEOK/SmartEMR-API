from .BaseDTO import BaseDTO
from typing import Optional

class ChartCommonCodeDTO(BaseDTO):
    CCCM_Idx : Optional[int] = None
    CCCG_Idx : Optional[int] = None
    CCC_Idx : Optional[int] = None
    CCCM_Cd : Optional[str] = None
    CCCM_Name : Optional[str] = None
    CCCG_Cd : Optional[str] = None
    CCCG_Name : Optional[str] = None
    CCC_Cd : Optional[str] = None
    CCC_Name : Optional[str] = None

class ChartCommonCode_Req(ChartCommonCodeDTO):
    pass

class ChartCommonCode_Res(ChartCommonCodeDTO):
    pass