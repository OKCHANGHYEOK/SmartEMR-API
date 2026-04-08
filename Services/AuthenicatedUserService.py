from contextvars import ContextVar
from Entities import MemberUser
from Exceptions import ApiException

class AuthenticatedUserService:
    def __init__(self):
        self.AuthUser = ContextVar("AuthUser", default=None)

    def SetUser(self, item : MemberUser):
        self.AuthUser = item

    def GetUser(self):
        user = self.AuthUser.get()
        if not user:
            raise ApiException("Cannot find a authenticated user.") 
        return user       