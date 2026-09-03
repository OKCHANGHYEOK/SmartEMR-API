from .BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean, DECIMAL
from sqlalchemy.dialects.mssql import NVARCHAR

class Consultation(BaseEntity):
    __tablename__ = 'Consultation'

    CST_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Idx = Column(Integer)
    MUR_Idx = Column(Integer)
    MUR_Idx_DOC = Column(Integer)
    PAT_Idx = Column(Integer)
    RCP_Idx = Column(Integer)
    IRC_Idx = Column(Integer)
    CST_InsuranceType = Column(String(3))
    CST_VisitType = Column(String(3))
    CST_Status = Column(String(3))
    CST_PayStatus = Column(String(3))
    CST_TreatResult = Column(String(3))
    CST_Subject = Column(String(3))
    CST_SubjectName = Column(String(20))
    CST_StartTime = Column(String(8))
    CST_EndTime = Column(String(8))
    CST_TotalPrice = Column(DECIMAL(10, 0))
    CST_InsuredPrice = Column(DECIMAL(10, 0))
    CST_NonInsurecPrice = Column(DECIMAL(10, 0))
    CST_OwnPatientPrice = Column(DECIMAL(10, 0))
    CST_PaidPrice = Column(DECIMAL(10, 0))
    CST_RemainPrice = Column(DECIMAL(10, 0))
    CST_Opinion = Column(NVARCHAR(None))
    CST_Memo = Column(String(500))
    CST_Date = Column(String(20))
    CST_YYMMDD = Column(String(10))
    CST_IsValid = Column(Boolean)
    CSTO_Property = Column(String)

    PAT_Name = Column(String(50))
    PAT_ChartNo = Column(String(20))
    PAT_Sex = Column(String(1))
    PAT_Age = Column(Integer)