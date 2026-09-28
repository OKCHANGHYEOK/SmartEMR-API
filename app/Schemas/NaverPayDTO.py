from .BaseDTO import BaseDTO
from typing import Optional

class NaverPayDTO(BaseDTO):
    NPY_Idx : Optional[int] = None
    PAYI_Idx : Optional[int] = None
    paymentId : Optional[str] = None
    payHistId : Optional[str] = None
    merchantName : Optional[str] = None
    merchantPayKey : Optional[str] = None
    merchantUserKey : Optional[str] = None
    admissionTypeCode : Optional[str] = None
    admissionYmdt : Optional[str] = None
    tradeConfirmYmdt : Optional[str] = None
    admissionState : Optional[str] = None
    totalPayAmount : Optional[int] = None
    applyPayAmount : Optional[int] = None
    primaryPayAmount : Optional[int] = None
    npointPayAmount : Optional[int] = None
    giftCardAmount : Optional[int] = None
    discountPayAmount : Optional[int] = None
    taxScopeAmount : Optional[int] = None
    taxExScopeAmount : Optional[int] = None
    environmentDepositAmount : Optional[int] = None
    primaryPayMeans : Optional[str] = None
    cardCorpCode : Optional[str] = None
    cardInstCount : Optional[int] = None
    usedCardPoint : Optional[bool] = None
    bankCorpCode : Optional[str] = None
    productName : Optional[str] = None
    
class NaverPay_Req(NaverPayDTO):
    clientId : Optional[str] = None
    clientSecret : Optional[str] = None
    chainId : Optional[str] = None
    IdempotencyKey : Optional[str] = None

class NaverPay_Res(NaverPayDTO):
    pass   