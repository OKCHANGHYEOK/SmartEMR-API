from typing import Generic, TypeVar, List, Optional, Type, get_args
from Schemas.BaseDTO import BaseDTO
from Common.Enums import eResponseCode

T = TypeVar("T", bound=BaseDTO)

class DataResponse(BaseDTO, Generic[T]):
    Item: Optional[T] = None
    Items: Optional[List[T]] = None
    Message: Optional[str] = ""
    ResponseCode : eResponseCode = eResponseCode.SUCCESS
    TotalCount: int = 0
    IsSuccess: bool = True

    @classmethod
    def CreateJsonResult(cls, 
                        items: Optional[List] = None, 
                        message: str = "", 
                        responseCode: eResponseCode = eResponseCode.SUCCESS,
                        isSuccess: bool = True):
        
        orig_bases = getattr(cls, "__orig_bases__", None)
        res_type = None
        
        if orig_bases:
            args = get_args(orig_bases[0])
            if args:
                res_type = args[0]

        retItems = []

        if items:
            for row in items:
                # 이미 pydantic 모델 인스턴스라면 그대로 쓰고, 아니라면 validate 수행
                if res_type and not isinstance(res_type, TypeVar):
                    if isinstance(row, res_type):
                        retItems.append(row)
                    else:
                        try:
                            retItems.append(res_type.model_validate(row))
                        except Exception:
                            # 검증 실패 시 방어 코드 (딕셔너리나 원래 값을 넣거나 로그 처리)
                            retItems.append(row) 
                else:
                    retItems.append(row)

        # 만약 Pydantic 모델 내에서 검증 에러가 발생하는 것을 방지하기 위해 
        # model_validate 대신 model_construct를 쓰거나 필드 매핑을 확인해야 합니다.
        return cls(
            Item=retItems[0] if len(retItems) == 1 else None,
            Items=retItems,
            Message=message,
            responseCode=responseCode,
            IsSuccess=isSuccess,
            TotalCount=len(retItems)
        )