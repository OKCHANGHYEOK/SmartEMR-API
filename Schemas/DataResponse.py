# Entities/DataResponse.py
from Schemas.BaseDTO import BaseDTO
from typing import Generic, TypeVar, List, Optional, Type

T = TypeVar("T", bound=BaseDTO) 

class DataResponse(BaseDTO, Generic[T]): 
    Item: Optional[T] = None
    Items: Optional[List[T]] = None
    Message: Optional[str] = ""
    TotalCount: int = 0
    IsSuccess: bool = True

    # Factory Method: DB 결과를 받아서 DTO로 변환하며 응답 객체 생성
    @classmethod
    def CreateJsonResult(cls, 
               res_type: Type[T] = type(T),
               item: Optional[T] = None, 
               items: Optional[List] = None, 
               message: str = "", 
               isSuccess: bool = True):
        
        # 여기서 실제 클래스(res_type)를 사용해 변환 작업을 수행합니다.
        retItems = [res_type.model_validate(row) for row in items] if items else []
        
        return cls(
            Item=item,
            Items=retItems,
            Message=message,
            IsSuccess=isSuccess,
            TotalCount=len(retItems)
        )
    