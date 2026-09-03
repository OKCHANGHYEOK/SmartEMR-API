from .BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL

class ConsultationOrder(BaseEntity):
    __tablename__ = 'ConsultationOrder'

    CSTO_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Idx = Column(Integer)
    MUR_Idx = Column(Integer)
    MUR_Idx_DOC = Column(Integer)
    PAT_Idx = Column(Integer)
    CST_Idx = Column(Integer)
    ORD_Idx = Column(Integer)
    ORDC_Cd = Column(String(3))
    ORDG_Cd = Column(String(3))
    ORDI_Cd = Column(String(3))
    CSTO_SugaCode = Column(String(8))
    CSTO_ClassCode = Column(String(30))
    CSTO_InsuranceType = Column(String(3))
    CSTO_Status = Column(String(3))
    CSTO_Name = Column(String(500))
    CSTO_Day = Column(Integer)
    CSTO_Count = Column(Integer)
    CSTO_Amount = Column(Integer)
    CSTO_UnitPrice = Column(DECIMAL(10, 0))
    CSTO_TotalPrice = Column(DECIMAL(10, 0))
    CSTO_Memo = Column(String(500))
    CSTO_Date = Column(String(20))
    CSTO_YYMMDD = Column(String(10))
    CSTO_IsValid = Column(Boolean)
    CSTO_Property = Column(String)