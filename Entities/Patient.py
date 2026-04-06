from Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean

class Patient(BaseEntity):
    __tablename__ = 'Patient'

    PAT_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Idx = Column(Integer)
    MUR_Idx = Column(Integer)
    PAT_Name = Column(String(50))
    PAT_ChartNo = Column(String(20))
    PAT_Sex = Column(String(1))
    PAT_Age = Column(Integer)
    PAT_BirthYear = Column(String(4))
    PAT_BirthMonth = Column(String(2))
    PAT_BirthDay = Column(String(2))
    PAT_RegisterNum1 = Column(String(6))
    PAT_RegisterNum2 = Column(String(100))
    PAT_Hpp1 = Column(String(10))
    PAT_Hpp2 = Column(String(10))
    PAT_Hpp3 = Column(String(10))
    PAT_Address1 = Column(String(10))
    PAT_Address2 = Column(String(100))
    PAT_Address3 = Column(String(100))
    PAT_Email = Column(String(50))
    PAT_FirstVisitDate = Column(String(10))
    PAT_LastVisitDate = Column(String(10))
    PAT_IsSolar = Column(String(1))
    PAT_IsAgreePersonalInfo = Column(String(1))
    PAT_IsForeign = Column(String(1))
    PAT_IsSMS = Column(String(1))
    PAT_IsEmail = Column(String(1))
    PAT_IsValid = Column(Boolean)