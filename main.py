import uvicorn
from fastapi import FastAPI, Depends
from MiddleWares import ExceptionMiddleWare
from Routers.LoginRouter import router as LoginRouter
from Routers import v1_router
from Services.Authentication import AuthenticateService
from Exceptions.Handlers import RegisterExceptionHandlers

app = FastAPI()

# 미들웨어 설정
app.middleware("http")(ExceptionMiddleWare.exceute)

# 라우터 설정
app.include_router(LoginRouter, prefix="/Login", tags=["Login"])
app.include_router(
    v1_router,
    dependencies=[Depends(AuthenticateService.AuthenticateUserByJWT)]
)

# 예외 핸들러 등록
RegisterExceptionHandlers(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)