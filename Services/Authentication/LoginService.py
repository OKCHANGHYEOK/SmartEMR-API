from fastapi import Depends
from Services.Domain import MemberUserService
from Services.Authentication import JWTService, HashService
from Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from Schemas.DataResponse import DataResponse
from Schemas.TokenResponse import TokenResponse
from Exceptions import ApiException

class LoginService:
    def __init__(self, _memberUserService : MemberUserService):
        self.memberUserService = _memberUserService

    async def login(self, item : MemberUser_Req):
        if item.MUR_Idx and not item.MUR_PassWord:
            ret = await self.memberUserService.GetMemberUser(item)
            
            if ret is None or not ret.Item:
                raise ApiException("디버깅 모드 로그인에 실패했습니다. 일치하는 유저가 없습니다.", status_code=404)\
                
            loginUser = ret.Item    

        else:    
            ret : DataResponse[MemberUser_Res]  = await self.memberUserService.GetMemberUserForLogin(item)

            if ret is None or ret.IsSuccess == False:
                raise ApiException("internal server error", status_code=500)
            
            loginUser = ret.Item

            if not loginUser:
                raise ApiException("no such user", status_code=404)

            if not HashService.VerifyPassword(item.MUR_PassWord, loginUser.MUR_PassWord):
                raise ApiException("incorrect password.", status_code=401)

        token = JWTService.CreateAccessToken(loginUser.MUR_Idx)

        return TokenResponse(AccessToken=token, TokenType="Bearer", ExpireMinutes=120, User=loginUser)
    
    async def GetHashedPassWord(self, request : MemberUser_Req):
        return {
            "HashedPassword" : HashService.HashPassword(request.MUR_PassWord)
        }