from enum import Enum

class eResponseCode(Enum):
    # 성공 관련
    SUCCESS = 200
    CREATE_SUCCESS = 201
    
    # 인증 관련 
    UNAUTHORIZED = 4001     # 인증 안됨
    TOKEN_EXPIRED = 4002    # 토큰 만료
    INVALID_TOKEN = 4003    # 유효하지 않은 토큰
    PERMISSION_DENIED = 4004 # 권한 부족
    
    # 비즈니스 로직 관련
    INVALID_PARAM = 5001 # 파라미터 오류
    DATA_NOTFOUND = 5002    # 데이터 없음
    DUPLICATE_DATA = 5003    # 중복 데이터
    
    # 서버 오류
    INTERNAL_SERVER_ERROR = 9999