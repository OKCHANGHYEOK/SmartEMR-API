from contextvars import ContextVar
from typing import Optional
from Entities import MemberUser
from Exceptions import ApiException
from Common.Enums import eResponseCode

class AuthenticatedUserService:
    def __init__(self):
        self.authUser = ContextVar[Optional[any]] = ContextVar("auth_user", default=None)

    def SetUser(self, item : MemberUser):
        self.authUser = item

    def GetUser(self):
        user = self.authUser.get()
        if not user:
            raise ApiException(
                    msg="Cannot find a authenticated user.",
                    res_code=eResponseCode.UNAUTHORIZED) 
        return user       