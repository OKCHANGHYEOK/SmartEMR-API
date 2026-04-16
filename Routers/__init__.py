import pkgutil
import importlib
from fastapi import APIRouter

v1_router = APIRouter()

# 인증이 필요 없는 라우터 목록
EXCLUDE_ROUTERS = ["LoginRouter"] 

for loader, moduleName, isPkg in pkgutil.walk_packages(__path__):
    # 제외 목록에 포함된 모듈은 건너뜁니다.
    if moduleName in EXCLUDE_ROUTERS:
        continue

    full_module_name = f"{__name__}.{moduleName}"
    module = importlib.import_module(full_module_name)

    if hasattr(module, "router"):
        prefix = f"/{moduleName.replace('Router', '')}"
        v1_router.include_router(module.router, prefix=prefix, tags=[moduleName])