from fastapi import Depends
from httpx import AsyncClient, Response
from app.Exceptions.ApiException import ApiException
from app.Entities.Pay import Pay
from app.Entities.NaverPay import NaverPay
from app.Services.Domain import BaseService
from app.Services.Domain import PayService
from app.Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from app.Schemas.DataResponse import DataResponse
from app.Schemas.PayDTO import Pay_Req, Pay_Res
from app.Schemas.NaverPayDTO import NaverPay_Req, NaverPay_Res
from app.Common import eSP
from app.Common.Enums import NaverPayResponseCode
from app.Config import settings

class NaverPayService(BaseService):
    def __init__(self, 
                 _authenticatedUserService : AuthenticatedUserService = Depends(AuthenticatedUserService),
                 _payService : PayService = Depends(PayService)):
        self.authenticatedUserService = _authenticatedUserService
        self.payService = _payService

    async def ApplyPayment(self, request : NaverPay_Req) -> DataResponse[NaverPay_Res]:
        user = self.authenticatedUserService.GetUser()

        if not user:
            raise ApiException("유저가 올바르지 않습니다.")
        
        result = await self.ApplyNaverPaymentAsync(request.paymentId)

        detail = result['body']['detail']
        
        if not detail:
            raise ApiException(f"네이버페이 결제승인 실패. 응답 데이터가 올바르지 않습니다.")
        
        item : NaverPay = NaverPay()
        item.NPY_Idx = request.NPY_Idx
        item.PAYI_Idx = request.PAYI_Idx
        item.paymentId = request.paymentId
        
        item.payHistId = detail['payHistId']
        item.merchantName = detail['merchantName']
        item.merchantPayKey = detail['merchantPayKey']
        item.merchantUserKey = detail['merchantUserKey']
        item.admissionTypeCode = detail['admissionTypeCode']
        item.admissionYmdt = detail['admissionYmdt']
        item.tradeConfirmYmdt = detail['tradeConfirmYmdt']
        item.admissionState = detail['admissionState']
        item.totalPayAmount = detail['totalPayAmount']
        item.applyPayAmount = detail['applyPayAmount']
        item.primaryPayAmount = detail['primaryPayAmount']
        item.npointPayAmount = detail['npointPayAmount']
        item.giftCardAmount = detail['giftCardAmount']
        item.discountPayAmount = detail['discountPayAmount']
        item.taxScopeAmount = detail['taxScopeAmount']
        item.taxExScopeAmount = detail['taxExScopeAmount']
        item.environmentDepositAmount = detail['environmentDepositAmount']
        item.primaryPayMeans = detail['primaryPayMeans']
        item.cardCorpCode = detail['cardCorpCode']
        item.cardInstCount = detail['cardInstCount']
        item.usedCardPoint = detail['usedCardPoint']
        item.bankCorpCode = detail['bankCorpCode']
        item.productName = detail['productName']

        ret = await self.DbContext.GetItem[NaverPay_Res](eSP.proc_NaverPay_SetNaverPay, item)
        
        if not ret or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)

        return DataResponse[NaverPay_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)
    
    async def ApplyNaverPaymentAsync(self, paymentId : str) -> Response:
        if not paymentId:
            raise ApiException("결제승인번호가 올바르지 않습니다.")
        
        headers = {
            "X-Naver-Client-Id": settings.naverpay.client_id,
            "X-Naver-Client-Secret": settings.naverpay.client_secret,
            "X-NaverPay-Chain-Id": settings.naverpay.chain_id,
            "X-NaverPay-Idempotency-Key": self.CreateIdempotencyKey(paymentId),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        data = {
            "paymentId": paymentId
        }
        
        async with AsyncClient() as client:
            result = await client.post(settings.naverpay.apply_url, headers=headers, data=data)

            if result.status_code != 200:
                raise ApiException(f"네이버페이 결제승인 실패. 응답이 올바르지 않습니다.")

            response = result.json()

            if response['code'] != NaverPayResponseCode.Success.value:
                raise ApiException(f"네이버페이 결제승인 실패. 서버 내부 오류가 발생했습니다. {response['message']}")

            return response

    def CreateIdempotencyKey(self, paymentId : str) -> str:
        if not paymentId:
            raise ApiException("결제승인번호가 올바르지 않습니다.")
        
        return f"{paymentId}-{self.authenticatedUserService.GetUser().MEM_Idx}-{self.authenticatedUserService.GetUser().MUR_Idx}"