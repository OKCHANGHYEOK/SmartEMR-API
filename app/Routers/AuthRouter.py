from fastapi import Depends
from app.Routers.BaseRouter import router
from app.Common import Common
from app.Infrastructure.EmailSerivce import EmailService
from app.Services.Authentication.JWTService import JWTService
from app.Services.Authentication.TokenService import TokenService
from app.Services.Domain import MemberUserService
from app.Schemas.TokenDTO import Token_Req, Token_Res
from app.Schemas.TokenResponse import TokenResponse
from app.Schemas.DataResponse import DataResponse
from app.Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from app.Exceptions import ApiException

class AuthRouter():
    @router.post("/RequestVerifyCode")
    async def RequestVerifyCode(request : dict, emailService : EmailService = Depends(EmailService),):
        MUR_Email : str = request.get("MUR_Email")

        if not MUR_Email:
            raise ApiException("이메일이 올바르지 않습니다.")

        isSuccess = await emailService.SendVerificationCodeAsync(recipient=MUR_Email, verify_code=Common.GenerateVerificationCode())

        if not isSuccess:
            raise ApiException("이메일 발송에 실패했습니다.")

        return DataResponse[object].CreateDefaultResult()

    @router.post("/refresh_access_token")
    async def RefreshToken(request : Token_Req,                
                           jwtService : JWTService = Depends(JWTService),                       
                           tokenService : TokenService = Depends(TokenService),
                           memberUserService : MemberUserService = Depends(MemberUserService)):
        try:
            payload = jwtService.DecodeToken(request.TOKEN_VALUE)
        except ApiException:
            raise ApiException("invalid refreshToken.")  

        if not payload:
            raise ApiException("토큰이 올바르지 않습니다.")
        
        retRefreshToken = await tokenService.GetRefreshToken(request)

        if not retRefreshToken:
            raise ApiException("cannot found a refreshToken.")
        
        MURItem = MemberUser_Req(MUR_Idx=request.MUR_Idx)

        response = await memberUserService.GetMemberUser(MURItem)
        
        if not response:
            raise ApiException("존재하지 않거나 삭제된 사용자입니다.", res_code=404)
        
        loginUser = response.Item

        new_access_token = jwtService.CreateAccessToken(loginUser)

        return TokenResponse(
            AccessToken=new_access_token,
            RefreshToken=request.TOKEN_VALUE,
            TokenType="Bearer",
            ExpireMinutes=120
        )