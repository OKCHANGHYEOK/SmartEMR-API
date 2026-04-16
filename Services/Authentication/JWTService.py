import jwt
from datetime import datetime, timedelta, timezone
from Config import settings

class JWTService:
    @staticmethod
    def CreateAccessToken(MUR_Idx : int, additionalClaims : dict = None) -> str:
        """
            사용자 ID와 추가 정보를 담은 JWT 액세스 토큰 생성
        """

        # 페이로드 구성
        payload = {
            "sub" : str(MUR_Idx),
            "iat" : datetime.now(timezone.utc),
            "exp" : datetime.now(timezone.utc) + timedelta(minutes=settings.jwt.token_expire_minutes)
        }

        # 추가정보가 있다면 병합
        if additionalClaims:
            payload.update(additionalClaims)

        # 토큰 서명 및 생성
        token = jwt.encode(
            payload,
            settings.jwt.secret_key,
            algorithm=settings.jwt.algorithm
        )    

        return token