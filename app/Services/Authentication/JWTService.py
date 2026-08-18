import jwt
from datetime import datetime, timedelta, timezone
from app.Config import settings
from app.Exceptions import ApiException
from app.Common.Enums import eResponseCode
from app.Entities.MemberUser import MemberUser

class JWTService:
    @staticmethod
    def CreateAccessToken(MURItem : MemberUser, additionalClaims : dict = None) -> str:
        """
            사용자 ID와 추가 정보를 담은 JWT 액세스 토큰 생성
        """

        # 페이로드 구성
        payload = {
            "sub" : f"{MURItem.MEM_Idx}|{MURItem.MUR_Idx}",
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
    
    @staticmethod
    def CreateRefreshToken(MURItem : MemberUser) -> str:
        payload = {
            "sub" : str(MURItem.MUR_Idx),
            "iat" : datetime.now(timezone.utc),
            "exp" : datetime.now(timezone.utc) + timedelta(days=settings.jwt.refresh_token_expire_days)
        }

        return jwt.encode(payload, settings.jwt.secret_key, algorithm=settings.jwt.algorithm)
    
    # 토큰 검증 및 해독
    @staticmethod
    def DecodeToken(token : str) -> dict:
        try:
            payload = jwt.decode(
                token,
                settings.jwt.secret_key,
                algorithms=[settings.jwt.algorithm]
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise ApiException("Token has expired.", res_code=eResponseCode.TOKEN_EXPIRED)
        
        except jwt.InvalidTokenError:
            raise ApiException("Invalid token.", res_code=eResponseCode.UNAUTHORIZED)