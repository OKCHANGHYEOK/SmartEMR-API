from fastapi import Depends
from app.Routers.BaseRouter import router
from app.Services.Authentication.JWTService import JWTService
from app.Services.Authentication.TokenService import TokenService
from app.Services.Domain import MemberUserService
from app.Schemas.TokenDTO import Token_Req, Token_Res
from app.Schemas.TokenResponse import TokenResponse
from app.Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from app.Exceptions import ApiException

class AuthRouter():
    @router.post("/refresh_access_token")
    async def RefreshToken(request : Token_Req, 
                       _jwtservice : JWTService = Depends(JWTService),
                       _tokenService : TokenService = Depends(TokenService),
                       _memberUserService : MemberUserService = Depends(MemberUserService)):
        try:
            payload = JWTService.DecodeToken(request.TOKEN_VALUE)
        except ApiException:
            raise ApiException("invalid refreshToken.")  
        
        retRefreshToken = await _tokenService.GetRefreshToken(request)

        if not retRefreshToken:
            raise ApiException("cannot found a refreshToken.")
        
        MURItem = MemberUser_Req(MUR_Idx=request.MUR_Idx)

        response = await _memberUserService.GetMemberUser(MURItem)
        
        if not response:
            raise ApiException("존재하지 않거나 삭제된 사용자입니다.", res_code=404)
        
        loginUser = response.Item

        new_access_token = JWTService.CreateAccessToken(loginUser)

        return TokenResponse(
            AccessToken=new_access_token,
            RefreshToken=request.TOKEN_VALUE,
            TokenType="Bearer",
            ExpireMinutes=120
        )
