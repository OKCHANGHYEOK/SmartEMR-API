from fastapi import FastAPI
from MiddleWares import ExceptionMiddleWare
from Routers import v1_router

app = FastAPI()

# 미들웨어 설정
app.middleware("http")(ExceptionMiddleWare.exceute)

# 라우터 설정
app.include_router(v1_router)