from contextvars import ContextVar
from typing import Optional
from Entities.MemberUser import MemberUser
from Exceptions import ApiException
from Common.Enums import eResponseCode

class AuthenticatedUserService:
    _auth_user_var: ContextVar[Optional[MemberUser]] = ContextVar("auth_user", default=None)

    def GetUser(self) -> MemberUser:
        # self._auth_user_var 로 접근합니다.
        user = self._auth_user_var.get()
        
        if not user:
            raise ApiException(
                msg="Cannot find an authenticated user.",
                res_code=eResponseCode.UNAUTHORIZED
            ) 
        return user       
    
    def SetUser(self, item: MemberUser):
        # 현재 비동기 컨텍스트(요청)에 유저 정보를 안전하게 저장합니다.
        self._auth_user_var.set(item)