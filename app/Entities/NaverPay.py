from .BaseEntity import BaseEntity
from sqlalchemy import Column, Integer, String, Boolean, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column

class NaverPay(BaseEntity):
    __tablename__ = "NaverPay"

    NPY_Idx = Column(Integer, primary_key=True, autoincrement=True)
    PAYI_Idx = Column(Integer)

    paymentId = Column(String(50))
    payHistId = Column(String(50))
    merchantName = Column(String(50))
    merchantPayKey = Column(String(64))
    merchantUserKey = Column(String(50))
    admissionTypeCode = Column(String(2))
    admissionYmdt = Column(String(14))
    tradeConfirmYmdt = Column(String(50))
    admissionState = Column(String(10))
    totalPayAmount = Column(Integer)
    applyPayAmount = Column(Integer)
    primaryPayAmount = Column(Integer)
    npointPayAmount = Column(Integer)
    giftCardAmount = Column(Integer)
    discountPayAmount = Column(Integer)
    taxScopeAmount = Column(Integer)
    taxExScopeAmount = Column(Integer)
    environmentDepositAmount = Column(Integer)
    primaryPayMeans = Column(String(10))
    cardCorpCode = Column(String(10))
    cardInstCount = Column(Integer)
    usedCardPoint = Column(Boolean)
    bankCorpCode = Column(String(10))
    productName = Column(String(128))