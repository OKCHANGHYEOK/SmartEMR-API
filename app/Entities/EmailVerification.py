from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from app.Entities.BaseEntity import BaseEntity

class EmailVerification(BaseEntity):
    __tablename__ = 'EmailVerification'

    EV_Idx = Column(Integer, primary_key=True, autoincrement=True)
    EV_Purpose = Column(String(10))
    EV_Email = Column(String(50))
    EV_CodeHash = Column(String(100))
    EV_CreatedAt = Column(String(20))
    EV_ExpiredAt = Column(String(20))
    EV_AttemptCount = Column(Integer)
    EV_IsVerified = Column(Boolean)
    EV_IsValid = Column(Boolean)