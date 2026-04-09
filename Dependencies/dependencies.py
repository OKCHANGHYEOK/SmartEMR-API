from typing import Type, TypeVar
from fastapi import Depends
from Infrastructure import AppDBContext
from Common import LoggerService
from Services.Authentication import AuthenticatedUserService, AuthenticateService

# 제네릭 타입 선언
T = TypeVar("T")

# 프로그램에 필요한 모듈 선언
_loggerService = LoggerService.getLogger()
_AppDbContext = AppDBContext(_loggerService)

def GetAuthenticatedUserService() -> AuthenticatedUserService:
    return AuthenticatedUserService()

def GetAuthenticateService(authenticatedUserService: AuthenticatedUserService = Depends(GetAuthenticatedUserService)) -> AuthenticateService:
    return AuthenticateService(authenticatedUserService)

# 서비스 의존성 주입을 위한 공용 클래스
class ServiceProvider:
    def __init__(self, service_type : Type[T]):
        self.service_type = service_type

    def __call__(self) -> T:
        return self.service_type(_AppDbContext)    