from fastapi import Request, Depends
from Exceptions.ApiException import ApiException
from Common.Enums import eResponseCode
from Services.Authentication.AuthenticatedUserService import AuthenticatedUserService
from Services.Authentication.JWTService import JWTService
from Entities.MemberUser import MemberUser

class AuthenticateService:
    # 1. FastAPI가 이 클래스를 스스로 생성할 수 있도록 매개변수에 Depends()를 달아줍니다.
    def __init__(self, _authenticatedUserService: AuthenticatedUserService = Depends(AuthenticatedUserService)):
        self.authenticatedUserService = _authenticatedUserService           

    async def AuthenticateUserByJWT(self, request: Request):
        # 헤더에서 토큰 추출
        authorization = request.headers.get("Authorization")

        if not authorization or not authorization.startswith("Bearer "):
            raise ApiException("token was not given or invalid format.", res_code=eResponseCode.UNAUTHORIZED)
        
        token = authorization.split(" ")[1]

        try:
            # 토큰 해독 및 유저 정보 세팅
            decoded_token = JWTService.DecodeToken(token)

            arrToken = decoded_token.get('sub').split("|")

            if not arrToken or len(arrToken) < 2:
                raise ApiException("Error Occured While Parsing Token.", res_code=eResponseCode.INTERNAL_SERVER_ERROR)
            
            MEM_Idx = int(arrToken[0])
            MUR_Idx = int(arrToken[1])
            
            # 유저 정보 추출 (예시)
            user = MemberUser(MEM_Idx=MEM_Idx, MUR_Idx=MUR_Idx)

            # 🌟 오타 수정: autenticated -> authenticated ('h' 추가)
            self.authenticatedUserService.SetUser(user)

        except ApiException:
            # 이미 발생한 ApiException은 그대로 위로 던짐
            raise
        except Exception as E:
            # 시스템 에러나 AttributeError 등 진짜 버그는 로그로 찍어서 확인 가능하게 처리
            print(f"인증 과정 중 예기치 못한 에러 발생: {E}") 
            raise ApiException("invalid token", res_code=eResponseCode.TOKEN_EXPIRED)    


    # 🌟 2. 핵심 해결책: 라우터가 안전하게 사용할 수 있도록 '함수형 의존성 객체'를 하단에 선언합니다.
    async def verify_jwt_token(request: Request, auth_service: AuthenticateService = Depends()):
        """
        FastAPI가 auth_service(클래스)를 Depends로 먼저 온전히 주입(인스턴스화)한 뒤,
        인증 메서드를 호출하므로 self 관련 422 에러가 완벽히 차단됩니다.
        """
        await auth_service.AuthenticateUserByJWT(request)