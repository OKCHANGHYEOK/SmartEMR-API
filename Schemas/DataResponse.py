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
                        item: Optional[T] = None, 
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
        
        # 💡 res_type을 정상적으로 찾았고, TypeVar가 아닐 때만 model_validate를 수행합니다.
        if res_type and not isinstance(res_type, TypeVar):
            try:
                retItems = [res_type.model_validate(row) for row in items] if items else []
            except Exception:
                # 변환 실패 시 방어 코드로 원본 데이터 유지
                retItems = items if items else []
        else:
            # 💡 [핵심] res_type이 None이거나 찾지 못했다면, 변환을 생략하고 원본 데이터를 그대로 사용합니다!
            retItems = items if items else [] 

        return cls(
            Item=(item if item else retItems[0] if retItems else None),
            Items=retItems,
            Message=message,
            responseCode=responseCode,
            IsSuccess=isSuccess,
            TotalCount=len(retItems)
        )