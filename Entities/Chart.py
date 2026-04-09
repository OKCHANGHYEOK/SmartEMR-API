from Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Numeric

class Chart(BaseEntity):
    __tablename__ = "Chart"

    CHT_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Idx = Column(Integer)
    MUR_Idx_DOC = Column(Integer)
    MUR_Idx_STF = Column(Integer)
    PAT_Idx = Column(Integer)
    PAT_ChartNo = Column(String(20))
    PAT_Name = Column(String(50))
    PAT_Sex = Column(String(1))
    CHT_VisitType = Column(Integer)
    CHT_CHTType = Column(String(10))
    CHT_Status = Column(String(10))
    CHT_Order = Column(Integer)
    CHT_Route = Column(String(20))
    CHT_Subject = Column(String(10))
    CHT_SubjectName = Column(String(50))
    CHT_InsuranceType = Column(String(10))
    CHT_MainSympTom = Column(Text)
    CHT_Diagnosis = Column(Text)
    CHT_StartDate = Column(DateTime)
    CHT_EndDate = Column(DateTime)
    CHT_TotalPrice = Column(Numeric(18, 0))
    CHT_Date = Column(String(20))
    CHT_YYMMDD = Column(String(10))
    CHT_IsValid = Column(Boolean)