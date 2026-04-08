import time
from fastapi import Request
from Dependencies.dependencies import _loggerService
from Exceptions.ApiException import ApiException
from Common.Enums import eResponseCode

async def exceute(request : Request, callNext):
    sTime = time.time()

    try:
        # 다음 파이프라인 실행
        response = await callNext(request)

        # 실행 시간 기록
        process_time = time.time() - sTime
        response.headers["X-Proccess-Time"] = str(process_time)

        return response
    
    except ApiException as exc:
        process_time = time.time() - sTime

        # 에러 로깅
        _loggerService.error(f"Request Failed: {request.method} {request.url}")
        _loggerService.error(f"Error Detail: {str(exc)}", exc_info=True)
    
        response = exc.response

        if response.ResponseCode is None:
            response.ResponseCode = eResponseCode.INTERNAL_SERVER_ERROR 

        # 실패 응답 반환
        return exc.response