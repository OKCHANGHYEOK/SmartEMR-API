from typing import TypeVar
from app.Common import LoggerService

# 제네릭 타입 선언
T = TypeVar("T")

# 프로그램에 필요한 모듈 선언
_loggerService = LoggerService.getLogger()