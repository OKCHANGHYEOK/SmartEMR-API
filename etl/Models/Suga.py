from app.Entities.BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, DateTime, Boolean

class Suga(BaseEntity):
    __tablename__ = 'Suga'

    SUGA_Idx = Column(Integer, primary_key=True, autoincrement=True)
    SUGA_Code = Column(String(8))
    SUGA_ClassCode = Column(String(30))
    SUGA_InsuranceType = Column(String(3))
    SUGA_SugeryType = Column(String(3))
    SUGAC_Cd = Column(String(3))
    SUGAG_Cd = Column(String(3))
    SUGAI_Cd = Column(String(3))
    SUGA_Name = Column(String(200))
    SUGA_Price = Column(Integer)
    SUGA_ClinicPrice = Column(Integer)
    SUGA_HospitalPrice = Column(Integer)
    SUGA_DentistPrice = Column(Integer)
    SUGA_HealthPrice = Column(Integer)
    SUGA_BirthCenterPrice = Column(Integer)
    SUGA_KorMedicinePrice = Column(Integer)
    SUGA_EffectiveFromDay = Column(DateTime)
    SUGA_EffectiveToDay = Column(DateTime)
    SUGA_IsUse = Column(Boolean)
    SUGA_Property = Column(String)

    def __repr__(self):
        return f"{self.SUGA_Code}/{self.SUGA_ClassCode}/{self.SUGA_InsuranceType}/{self.SUGA_SugeryType}/{self.SUGAC_Cd}/{self.SUGA_Name}/{self.SUGA_ClinicPrice}/{self.SUGA_HospitalPrice}/{self.SUGA_DentistPrice}/{self.SUGA_BirthCenterPrice}/{self.SUGA_KorMedicinePrice}/{self.SUGA_EffectiveFromDay}"