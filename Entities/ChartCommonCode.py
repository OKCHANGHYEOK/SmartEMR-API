from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from Entities.BaseEntity import BaseEntity

class ChartCommonCode_Req(BaseEntity):
    CCC_Idx = Column(Integer, primary_key=True, autoincrement=True)
    CCCM_Idx = Column(Integer)
    CCCG_Idx = Column(Integer)
    CCCM_Cd = Column(String(10))
    CCCG_Cd = Column(String(10))
    CCC_Cd = Column(String(10))

class ChartCommonCode_Res(BaseEntity):
    CCC_Idx = Column(Integer, primary_key=True, autoincrement=True)
    CCCM_Idx = Column(Integer)
    CCCG_Idx = Column(Integer)
    CCCM_Cd = Column(String(10))
    CCCG_Cd = Column(String(10))
    CCC_Cd = Column(String(10))
    CCCM_Name = Column(String(10))
    CCCG_Name = Column(String(10))
    CCC_Name = Column(String(10))    