from fastapi import Request, Depends
from Exceptions.ApiException import ApiException
from Common.Enums import eResponseCode
from Services.Authentication import AuthenticatedUserService
from Entities import MemberUser

class AuthenticateService:
    def __init__(self, _authenticatedUserService: AuthenticatedUserService):
        self.authenticatedUserService = _authenticatedUserService           

    async def AuthenticateUserByJWT(self, request : Request):
        # 헤더에서 토큰 추출
        authorization = request.headers.get("Authorization")

        if not authorization or not authorization.startswith("Bearer "):
            raise ApiException("token was not given or invalid format.", res_code=eResponseCode.UNAUTHORIZED)
        
        token = authorization.split(" ")[1]

        try:
            # 토큰 검증

            # 유저 정보 추출
            user : MemberUser = None

            # 서비스에 저장
            self.autenticatedUserService.SetUser(user)

        except Exception as E:
            raise ApiException("invalid token", res_code=eResponseCode.TOKEN_EXPIRED)    

