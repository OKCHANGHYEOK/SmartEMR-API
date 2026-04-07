from Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean

class Member(BaseEntity):
    MEM_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Name = Column(String(100), nullable=False)
    MEM_MediNo = Column(String(20))
    MEM_BizNum = Column(String(20))
    MEM_BizType = Column(String(20))
    MEM_Address = Column(String(100))
    MEM_Address1 = Column(String(10))
    MEM_Address2 = Column(String(100))
    MEM_Address3 = Column(String(100))
    MEM_Tel1 = Column(String(10))
    MEM_Tel2 = Column(String(10))
    MEM_Tel3 = Column(String(10))
    MEM_StartDate = Column(String(10))
    MEM_EndDate = Column(String(10))
    MEM_OperationStatus = Column(Integer, default=1)
    MEM_AdminUser = Column(Integer, default=0)
    MEM_Date = Column(String(20))
    MEM_YYMMDD = Column(String(10))
    MEM_IsValid = Column(Boolean)