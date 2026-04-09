from fastapi import FastAPI, Depends
from MiddleWares import ExceptionMiddleWare
from Routers import v1_router
from Services.Authentication import AuthenticateService
from Exceptions.Handlers import RegisterExceptionHandlers

app = FastAPI()
# app = FastAPI(dependencies=[Depends(AuthenticateService.AuthenticateUserByJWT)])

# 미들웨어 설정
app.middleware("http")(ExceptionMiddleWare.exceute)

# 라우터 설정
app.include_router(v1_router)

# 예외 핸들러 등록
RegisterExceptionHandlers(app)