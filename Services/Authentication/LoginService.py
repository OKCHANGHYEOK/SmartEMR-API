from fastapi import Depends
from Services.Domain import MemberUserService
from Services.Authentication import JWTService, HashService
from Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from Schemas.DataResponse import DataResponse
from Exceptions import ApiException

class LoginService:
    def __init__(self, _memberUserService : MemberUserService):
        self.memberUserService = _memberUserService

    async def login(self, item : MemberUser_Req):
        ret : DataResponse[MemberUser_Res]  = await self.memberUserService.GetMemberUserForLogin(item)

        if ret is None or ret.IsSuccess == False:
            raise ApiException("internal server error", status_code=500)
        
        loginUser = ret.Item

        if not loginUser:
            raise ApiException("no such user", status_code=404)

        if not HashService.VerifyPassword(item.MUR_PassWord, loginUser.MUR_PassWord):
            raise ApiException("incorrect password.", status_code=401)

        token = JWTService.CreateAccessToken(
            userId = loginUser.MUR_Id,
            additionalClaims = {
                "MEM_Idx" : loginUser.MEM_Idx
            }
        )

        return {
            "AccessToken" : token,
            "TokenType" : "bearer"
        }
    
    async def GetHashedPassWord(self, request : MemberUser_Req):
        return {
            "HashedPassword" : HashService.HashPassword(request.MUR_PassWord)
        }