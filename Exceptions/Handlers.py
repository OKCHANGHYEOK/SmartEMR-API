from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .ApiException import ApiException

def RegisterExceptionHandlers(app : FastAPI):
    """
        애플리케이션의 모든 커스텀 예외 핸들러 등록
    """

    @app.exception_handler(ApiException)
    async def ApiExceptionHandler(request : Request, exc : ApiException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success" : False,
                "message" : exc.message,
                "responseCode" : exc.responseCode.value
            }
        )