from typing import Generic, TypeVar, List, Optional, Type, get_args
from Schemas.BaseDTO import BaseDTO

T = TypeVar("T", bound=BaseDTO)

class DataResponse(BaseDTO, Generic[T]):
    Item: Optional[T] = None
    Items: Optional[List[T]] = None
    Message: Optional[str] = ""
    TotalCount: int = 0
    IsSuccess: bool = True

    @classmethod
    def CreateJsonResult(cls, 
                         items: Optional[List] = None, 
                         item: Optional[T] = None, 
                         message: str = "", 
                         isSuccess: bool = True):
        
        orig_bases = getattr(cls, "__orig_bases__", None)
        res_type = None
        
        if orig_bases:
            # DataResponse[Member_Res]에서 Member_Res 타입을 추출
            args = get_args(orig_bases[0])
            if args:
                res_type = args[0]

        # 만약 타입을 찾았다면 model_validate를 수행합니다.
        # TypeVar 객체인지 실제 클래스인지 확인하는 방어 로직
        if res_type and not isinstance(res_type, TypeVar):
            retItems = [res_type.model_validate(row) for row in items] if items else []
        else:
            # 타입을 찾지 못한 경우 (그냥 DataResponse.CreateJsonResult() 호출 시)
            retItems = items if items else []

        return cls(
            Item=item,
            Items=retItems,
            Message=message,
            IsSuccess=isSuccess,
            TotalCount=len(retItems)
        )