from .BaseDTO import BaseDTO
from typing import Optional
from Schemas.InsuranceDTO import Insurance_Req

class ReceptionDTO(BaseDTO):
    RCP_Idx : Optional[int] = None
    PAT_Idx: Optional[int] = None
    MEM_Idx: Optional[int] = None
    MUR_Idx: Optional[int] = None
    MUR_Idx_DOC: Optional[int] = None
    MUR_Idx_STF: Optional[int] = None
    RES_Idx : Optional[int] = None
    PAT_Name: Optional[str] = None
    PAT_ChartNo: Optional[str] = None
    PAT_Sex: Optional[str] = None
    PAT_Age: Optional[int] = None
    RCP_Status : Optional[str] = None
    RCP_Route : Optional[str] = None
    RCP_VisitType : Optional[str] = None
    RCP_Subject : Optional[str] = None
    RCP_SubjectName : Optional[str] = None
    RCP_ReceiptDate : Optional[str] = None
    RCP_ReceiptTime : Optional[str] = None
    RCP_StartTreatTime : Optional[str] = None
    RCP_EndTreatTime : Optional[str] = None
    RCP_Memo : Optional[str] = None
    RCP_IsValid : Optional[bool ] = None

class Reception_Req(ReceptionDTO):
    IRCItem : Optional[Insurance_Req] = None
    pass

class Reception_Res(ReceptionDTO):
    MUR_Name_DOC : Optional[str] = None
    PAT_IsSMS: Optional[str] = None