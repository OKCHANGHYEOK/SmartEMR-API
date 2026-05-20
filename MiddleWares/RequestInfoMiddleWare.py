import json
from fastapi import FastAPI, Request

async def LogRequestBody(request : Request, call_next):
    body = await request.body()

    if body:
        try:
            parsed_json = json.loads(body.decode('utf-8'))
            print("\n" + "="*50)
            print(f"📡 [수신 요청] 경로: {request.url.path}")
            print("📦 [Request Body]:")
            print(json.dumps(parsed_json, indent=4, ensure_ascii=False))
            print("="*50 + "\n")
        except Exception:
            print(f"📦 [Request Body (Raw)]: {body.decode('utf-8')}")

    response = await call_next(request)

    return response