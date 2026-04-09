from fastapi import Depends
from Services.Domain import MemberUserService
from Dependencies.dependencies import ServiceProvider
from Entities.MemberUser import MemberUser
from Schemas.MemberUserDTO import MemberUser_Req
from Exceptions import ApiException
from Authentication import JWTService, HashService

class LoginService:
    def __init__(self, _memberUserService : MemberUserService = Depends(ServiceProvider(MemberUserService))):
        self.memberUserSerivce = _memberUserService

    async def login(self, item : MemberUser_Req):
        loginUser : MemberUser = await self.memberUserSerivce.GetMemberUserForLogin(item)

        if not loginUser:
            raise ApiException("no such user", status_code=404)

        if not HashService.HashPassword(item.MUR_Password, loginUser.MUR_Password):
            raise ApiException("incorrect password.", status_code=401)

        return JWTService.CreateAccessToken(
            userId = loginUser.MUR_Id,
            additionalClaims = {
                "MEM_Idx" : loginUser.MEM_Idx
            }
        )