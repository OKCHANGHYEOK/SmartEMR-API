from Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean

class Pay(BaseEntity):
    __tablename__ = 'Pay'

    PAY_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Idx = Column(Integer)
    MUR_Idx = Column(Integer)
    PAT_Idx = Column(Integer)
    CST_Idx = Column(Integer)
    PAY_Status = Column(String(3))
    PAY_AMOUNT_TOT = Column(DECIMAL(10, 0), default=0)
    PAY_AMOUNT_INSURED = Column(DECIMAL(10, 0), default=0)
    PAY_AMOUNT_NONINSURED = Column(DECIMAL(10, 0), default=0)
    PAY_AMOUNT_PATIENT = Column(DECIMAL(10, 0), default=0)
    PAY_AMOUNT_PAID = Column(DECIMAL(10, 0), default=0)
    PAY_AMOUNT_REMAIN = Column(DECIMAL(10, 0), default=0)
    PAY_Date = Column(String(20))
    PAY_YYMMDD = Column(String(10))
    PAY_IsValid = Column(Boolean)
