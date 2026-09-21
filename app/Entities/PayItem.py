from app.Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean

class PayItem(BaseEntity):
    __tablename__ = 'PayItem'

    PAYI_Idx = Column(Integer, primary_key=True, autoincrement=True)
    PAY_Idx = Column(Integer)
    MEM_Idx = Column(Integer)
    MUR_Idx = Column(Integer)
    PAT_Idx = Column(Integer)
    PAYI_Type = Column(String(3))
    PAYI_Method = Column(String(3))
    PAYI_Price = Column(DECIMAL(10,0))
    PAYI_Time = Column(String(8))
    PAYI_Date = Column(String(20))
    PAYI_YYMMDD = Column(String(10))
    PAYI_IsValid = Column(Boolean)