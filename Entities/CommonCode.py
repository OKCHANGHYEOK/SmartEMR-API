from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from Entities.BaseEntity import BaseEntity

class CommonCode(BaseEntity):
    __tablename__ = 'CommonCode'

    CCC_Idx = Column(Integer, primary_key=True)
    CCG_Idx = Column(Integer)
    CCI_Idx = Column(Integer)
    CCC_Cd = Column(String(20))
    CCC_Name = Column(String(50))
    CCG_Cd = Column(String(20))
    CCG_Name = Column(String(59))
    CCI_Cd = Column(String(20))
    CCI_Name = Column(String(50))