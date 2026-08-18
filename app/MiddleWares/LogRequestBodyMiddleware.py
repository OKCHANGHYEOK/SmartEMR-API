from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class LogRequestBodyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. GET이나 DELETE처럼 바디가 없는 요청은 그냥 패스
        if request.method in ["GET", "DELETE"]:
            return await call_next(request)
        
        # 2. 바디 데이터를 한 번 읽습니다.
        body = await request.body()

        # 3. 로그 출력
        print(f"Request Body: {body.decode('utf-8')}")

        # 4. 🔥 핵심: 다음 단계에서 바디를 다시 읽을 수 있도록 새 스트림 객체로 덮어씁니다.
        async def receive():
            return {"type": "http.request", "body": body, "more_body": False}

        request._receive = receive

        # 5. 재포장된 request를 다음 미들웨어(AuthenticateUserByJWT)로 전달합니다.
        response = await call_next(request)

        return response