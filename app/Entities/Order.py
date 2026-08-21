from app.Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, DateTime, Boolean

class Order(BaseEntity):
    __tablename__ = 'Order'

    ORD_Idx = Column(Integer, primary_key=True, autoincrement=True)
    SUGA_Idx = Column(Integer)
    ORDC_Cd = Column(String(3))
    ORDG_Cd = Column(String(3))
    ORDI_Cd = Column(String(3))
    ORD_SugaCode = Column(String(3))
    ORD_ClassCode = Column(String(3))
    ORD_Name = Column(String(500))
    ORD_InsuranceType = Column(String(3))
    ORD_SurgeryType = Column(String(3))
    ORD_Price = Column(Integer)
    ORD_Source = Column(String(3))
    ORD_EffectiveFromDay = Column(DateTime)
    ORD_EffectiveToDay = Column(DateTime)
    ORD_IsUse = Column(Boolean)
    ORD_IsQuickOrder = Column(Boolean)