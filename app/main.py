import uvicorn
from fastapi import FastAPI, Depends
from app.MiddleWares import ExceptionMiddleWare, LogRequestBodyMiddleware
from app.Routers import v1_router
from app.Routers.LoginRouter import router as LoginRouter
from app.Routers.AuthRouter import router as AuthRouter
from app.Routers.MemberRouter import router as MemberRouter
from app.Routers.MemberUserRouter import router as MemberUserRouter
from app.Services.Authentication.AuthenticateService import AuthenticateService 
from app.Exceptions.Handlers import RegisterExceptionHandlers

app = FastAPI()

# 미들웨어 설정
app.add_middleware(ExceptionMiddleWare)
app.add_middleware(LogRequestBodyMiddleware)

# 라우터 설정
app.include_router(LoginRouter, prefix="/Login", tags=["Login"])
app.include_router(AuthRouter, prefix="/Auth", tags=["Auth"])
app.include_router(MemberRouter, prefix="/Member", tags=["Member"])
app.include_router(MemberUserRouter, prefix="/MemberUser", tags=["MemberUser"])
app.include_router(
    v1_router,
    dependencies=[Depends(AuthenticateService.verify_jwt_token)]
)

# 예외 핸들러 등록
RegisterExceptionHandlers(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)