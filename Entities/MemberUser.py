from Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean

class MemberUser(BaseEntity):
    __tablename__ = "MemberUser"

    MUR_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Idx = Column(Integer)
    MUR_Role = Column(String(3))
    vMUR_Role = Column(String(3))
    MUR_Id = Column(String(50))
    MUR_PassWord = Column(String(200))
    MUR_Name = Column(String(50))
    MUR_Gender = Column(String(1))
    vMUR_Gender = Column(String(1))
    MUR_Address1 = Column(String(50))
    MUR_Address2 = Column(String(50))
    MUR_Address3 = Column(String(50))
    MUR_Age = Column(Integer)
    MUR_BirthYear = Column(String(8))
    MUR_BirthMonth = Column(String(8))
    MUR_BirthDay = Column(String(8))
    MUR_PhoneNum1 = Column(String(10))
    MUR_PhoneNum2 = Column(String(10))
    MUR_PhoneNum3 = Column(String(10))
    MUR_Email = Column(String(50))
    MUR_Date = Column(String(50))
    MUR_YYMMDD = Column(String(20))
    MUR_IsValid = Column(Boolean)
