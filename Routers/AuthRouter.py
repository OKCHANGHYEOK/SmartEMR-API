from fastapi import APIRouter, Request, Depends
from Services.Authentication import JWTService
from Services.Authentication.TokenService import TokenService
from Services.Domain import MemberUserService
from Schemas.TokenDTO import Token_Req, Token_Res
from Schemas.TokenResponse import TokenResponse
from Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from Exceptions import ApiException

router = APIRouter()

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

    loginUser = await _memberUserService.GetMemberUser(MURItem).Item

    new_access_token = JWTService.CreateAccessToken(loginUser)

    return TokenResponse(
        AccessToken=new_access_token,
        RefreshToken=request.TOKEN_VALUE,
        TokenType="Bearer",
        ExpireMinutes=120
    )
