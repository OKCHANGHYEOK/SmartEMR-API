from typing import Type, TypeVar
from Infrastructure import AppDBContext
from Common import LoggerService
from Services.Authentication import AuthenticatedUserService, AuthenticateService, LoginService
from Services.Domain import MemberUserService, MemberService, PatientService

# 제네릭 타입 선언
T = TypeVar("T")

# 프로그램에 필요한 모듈 선언
_loggerService = LoggerService.getLogger()