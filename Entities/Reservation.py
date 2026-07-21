from Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean

class Reservation(BaseEntity):
    __tablename__ = 'Reservation'

    RES_Idx = Column(Integer, primary_key=True, autoincrement=True)
    PAT_Idx = Column(Integer)
    MEM_Idx = Column(Integer)
    MUR_Idx = Column(Integer)
    MUR_Idx_DOC = Column(Integer)
    MUR_Idx_STF = Column(Integer)
    PAT_Name = Column(String(50))
    PAT_ChartNo = Column(String(20))
    PAT_Sex = Column(String(1))
    PAT_Age = Column(Integer)
    RES_Status = Column(String(3))
    RES_Route = Column(String(3))
    RES_Subject = Column(String(10))
    RES_SubjectName = Column(String(50))
    RES_ReservationDate = Column(String(10))
    RES_ReserationTime = Column(String(8))
    RES_Memo = Column(String(500))
    RES_YYMMDD = Column(String(10))
    RES_IsValid = Column(Boolean)