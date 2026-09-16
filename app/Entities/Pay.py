from app.Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean

class Pay(BaseEntity):
    __tablename__ = 'Pay'

    PAY_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Idx = Column(Integer)
    MUR_Idx = Column(Integer)
    PAT_Idx = Column(Integer)
    CST_Idx = Column(Integer)
    CST_Status = Column(String(3))
    PAY_Status = Column(String(3))
    PAY_TotalPrice = Column(DECIMAL(10, 0), default=0)
    PAY_InsuredPrice = Column(DECIMAL(10, 0), default=0)
    PAY_NonInsuredPrice = Column(DECIMAL(10, 0), default=0)
    PAY_OwnPatientPrice = Column(DECIMAL(10, 0), default=0)
    PAY_PaidPrice = Column(DECIMAL(10, 0), default=0)
    PAY_RemainPrice = Column(DECIMAL(10, 0), default=0)
    PAY_Memo = Column(String(500))
    PAY_Date = Column(String(20))
    PAY_YYMMDD = Column(String(10))
    PAY_IsValid = Column(Boolean)
    
    PAT_Name = Column(String(50))
    PAT_ChartNo = Column(String(20))
    PAT_Age = Column(Integer)
    PAT_Sex = Column(String(1))
    
    
