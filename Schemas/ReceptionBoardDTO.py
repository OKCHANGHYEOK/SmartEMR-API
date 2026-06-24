from .BaseDTO import BaseDTO
from typing import Optional

class ReceptionBoardDTO(BaseDTO):
    RCP_Idx : Optional[int] = None
    RES_Idx : Optional[int] = None
    RCB_Type : Optional[str] = None
    MEM_Idx : Optional[int] = None
    MUR_Idx_DOC : Optional[int] = None
    MUR_Idx_STF : Optional[int] = None
    PAT_Idx : Optional[str] = None

    RCP_Status : Optional[str] = None
    RCP_InsuranceType : Optional[str] = None
    
    RES_Status : Optional[str] = None
    
    RCB_VisitType : Optional[str] = None
    RCB_Route : Optional[str] = None
    RCB_Subject : Optional[str] = None
    RCB_YYMMDD : Optional[str] = None

class ReceptionBoard_Req(ReceptionBoardDTO):
    pass

class ReceptionBoard_Res(ReceptionBoardDTO):
    RCB_SubjectName : Optional[str] = None
    RCB_Date : Optional[str] = None
    RCB_Time : Optional[str] = None
    RCB_Memo : Optional[str] = None
    MUR_Name_DOC : Optional[str] = None
    PAT_ChartNo : Optional[str] = None
    PAT_Name : Optional[str] = None
    PAT_Sex : Optional[str] = None
    PAT_Age : Optional[int] = None