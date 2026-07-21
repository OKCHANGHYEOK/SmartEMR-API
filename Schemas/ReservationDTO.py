from .BaseDTO import BaseDTO
from typing import Optional

class ReservationDTO(BaseDTO):
    RES_Idx : Optional[int] = None
    PAT_Idx : Optional[int] = None
    MEM_Idx : Optional[int] = None
    MUR_Idx : Optional[int] = None
    MUR_Idx_DOC : Optional[int] = None
    MUR_Idx_STF : Optional[int] = None
    PAT_Name : Optional[str] = None
    PAT_ChartNo : Optional[str] = None
    PAT_Sex : Optional[str] = None
    PAT_Age : Optional[int] = None
    RES_Status : Optional[str] = None
    RES_Route : Optional[str] = None
    RES_Subject : Optional[str] = None
    RES_SubjectName : Optional[str] = None
    RES_ReservationDate : Optional[str] = None
    RES_ReserationTime : Optional[str] = None
    RES_Memo : Optional[str] = None
    RES_YYMMDD : Optional[str] = None
    RES_IsValid : Optional[bool] = None

class Reservation_Req(ReservationDTO):
    pass

class Reservation_Res(ReservationDTO):
    MUR_Name_DOC : Optional[str] = None

    PAT_Name: Optional[str] = None
    PAT_ChartNo: Optional[str] = None
    PAT_Sex: Optional[str] = None
    PAT_Age: Optional[int] = None
    PAT_IsSMS: Optional[str] = None