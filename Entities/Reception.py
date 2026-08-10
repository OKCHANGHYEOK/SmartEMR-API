from Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean

class Reception(BaseEntity):
    __tablename__ = 'Reception'

    RCP_Idx = Column(Integer, primary_key=True, autoincrement=True)
    PAT_Idx = Column(Integer)
    MEM_Idx = Column(Integer)
    MUR_Idx = Column(Integer)
    MUR_Idx_DOC = Column(Integer)
    MUR_Idx_STF = Column(Integer)
    RES_Idx = Column(Integer)
    IRC_Idx = Column(Integer)
    PAT_Name = Column(String(50))
    PAT_ChartNo = Column(String(20))
    PAT_Sex = Column(String(1))
    PAT_Age = Column(Integer)
    RCP_Status = Column(String(3))
    RCP_Route = Column(String(3))
    RCP_VisitType = Column(String(3))
    RCP_InsuranceType = Column(String(3))
    RCP_Subject = Column(String(10))
    RCP_SubjectName = Column(String(50))
    RCP_ReceiptDate = Column(String(10))
    RCP_ReceiptTime = Column(String(8))
    RCP_StartTreatTime = Column(String(8))
    RCP_EndTreatTime = Column(String(8))
    RCP_Memo = Column(String(500))
    RCP_YYMMDD = Column(String(10))
    RCP_IsValid = Column(Boolean)
    