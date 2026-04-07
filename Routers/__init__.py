import pkgutil
import importlib
from fastapi import APIRouter

v1_router = APIRouter()

for loader, moduleName, isPkg in pkgutil.walk_packages(__path__):
    # 각 모듈을 동적으로 임포트
    full_module_name = f"{__name__}.{moduleName}"
    module = importlib.import_module(full_module_name)

    # 모듈 안에 router 객체가 있다면 v1_router 에 등록
    if hasattr(module, "router"):
        # 파일 이름을 prefix 로 사용
        prefix = f"{moduleName.replace('Router', '')}"
        v1_router.include_router(module.router, prefix=prefix, tags=[moduleName])