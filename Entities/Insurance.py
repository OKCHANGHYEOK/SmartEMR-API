from Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean

class Insurance(BaseEntity):
    __tablename__ = 'Insurance'

    IRC_Idx = Column(Integer, primary_key=True, autoincrement=True)
    MEM_Idx = Column(Integer)
    PAT_Idx = Column(Integer)
    RCP_Idx = Column(Integer)
    IRC_Type = Column(String(3))
    IRC_CertNum = Column(String(20))
    IRC_ContractorName = Column(String(20))
    IRC_InsuredName = Column(String(20))
    IRC_CoName = Column(String(20))
    IRC_EffectiveYYMMDD = Column(String(10))
    IRC_ExpiredYYMMDD = Column(String(10))
    IRC_IsValid = Column(Boolean)