from . import JWTService, HashService
from fastapi import Depends
from Services.Authentication.TokenService import TokenService
from Services.Domain import BaseService
from Services.Domain import MemberService
from Services.Domain import MemberUserService
from Schemas.MemberDTO import Member_Req, Member_Res
from Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from Schemas.DataResponse import DataResponse
from Schemas.TokenResponse import TokenResponse
from Schemas.TokenDTO import Token_Req, Token_Res
from Exceptions import ApiException
from Common.common import isNullOrWhiteSpace
from Common.eSP import eSP

class LoginService(BaseService):
    def __init__(self, 
                 _memberService : MemberService = Depends(MemberService), 
                 _memberUserService : MemberUserService = Depends(MemberUserService),
                 _tokenService : TokenService = Depends(TokenService)):
        self.memberService = _memberService
        self.memberUserService = _memberUserService
        self.tokenService = _tokenService

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

        # 회원사 정보 읽기
        retMEM : DataResponse[Member_Res] = await self.memberService.GetMember(Member_Req(MEM_Idx=loginUser.MEM_Idx))

        if not retMEM:
            raise ApiException("internal server error", status_cod=404)

        member = retMEM.Item

        access_token = JWTService.CreateAccessToken(loginUser)
        refresh_token = JWTService.CreateRefreshToken(loginUser)

        if isNullOrWhiteSpace(access_token) or isNullOrWhiteSpace(refresh_token):
            raise ApiException("failed to create token.", status_code=500)
        
        # 토큰 생성후 리프레쉬 토큰은 DB에 저장해둠
        setToken = Token_Req()
        setToken.RTK_Idx = 0
        setToken.MUR_Idx = loginUser.MUR_Idx
        setToken.TOKEN_VALUE = refresh_token
        setToken.ISREVOKED = False

        retToken = await self.tokenService.SetRefreshToken(setToken)

        if not retToken or not isNullOrWhiteSpace(self.DbContext.retMessage):
            raise ApiException("failed to save token.", status_code=500)

        return TokenResponse(AccessToken=access_token, 
                             RefreshToken=refresh_token,
                             TokenType="Bearer", 
                             ExpireMinutes=120, 
                             Member=member, 
                             User=loginUser)
    
    async def GetHashedPassWord(self, request : MemberUser_Req):
        return {
            "HashedPassword" : HashService.HashPassword(request.MUR_PassWord)
        }