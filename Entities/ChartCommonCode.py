from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from Entities.BaseEntity import BaseEntity

class ChartCommonCode(BaseEntity):
    __tablename__ = 'ChartCommonCode'

    CCC_Idx = Column(Integer, primary_key=True)
    CCCM_Idx = Column(Integer)
    CCCG_Idx = Column(Integer)
    CCCM_Cd = Column(String(20))
    CCCM_Name = Column(String(50))
    CCCG_Cd = Column(String(20))
    CCCG_Name = Column(String(59))
    CCC_Cd = Column(String(20))
    CCC_Name = Column(String(50))