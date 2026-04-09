from fastapi import FastAPI, Depends
from MiddleWares import ExceptionMiddleWare
from Routers import v1_router
from Services.AuthenticateService import AuthenticateService

app = FastAPI(dependencies=[Depends(AuthenticateService.AuthenticateUserByJWT)])

# 미들웨어 설정
app.middleware("http")(ExceptionMiddleWare.exceute)

# 라우터 설정
app.include_router(v1_router)