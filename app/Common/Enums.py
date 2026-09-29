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

class NaverPayResponseCode(Enum):
    Success = 'Success'                                     # 성공
    Fail = 'Fail'                                           # PG, 은행 및 기타 오류 발생 시
    InvalidMerchantAuth = 'InvalidMerchantAuth'                     # 유효하지 않은 가맹점인 경우
    TimeExpired = 'TimeExpired'                             # 결제 승인 가능 시간 초과 시 (10분 초과시)
    AlreadyOnGoing = 'AlreadyOnGoing'                       # 해당 결제번호로 결제가 이미 진행 중일 때
    AlreadyComplete = 'AlreadyComplete'                     # 해당 결제번호로 이미 결제가 완료되었을 때
    OwnerAuthFail = 'OwnerAuthFail'                         # 본인 카드 인증 오류 시
    BankMaintenance = 'BankMaintenance'                     # 충전 계좌 점검 시 
    NotEnoughAccountBalance = 'NotEnoughAccountBalance'     # 충전 계좌 잔고 부족
    MaintenanceOngoing = 'MaintenanceOngoing'               # 서비스 점검중
    FaultCheckOngoing = 'FaultCheckOngoing'                 # 원천사 시스템 점검으로 해당 결제수단을 이용할 수 없을 때

