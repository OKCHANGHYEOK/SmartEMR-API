from pydantic import BaseModel, ConfigDict
from typing import Optional

class BaseDTO(BaseModel):
    # API 요청 시 공통으로 들어오는 페이징/검색 필드
    sDay: Optional[str] = None
    eDay: Optional[str] = None
    keyword: Optional[str] = None
    PageIndex: Optional[int] = 1
    PageSize: Optional[int] = 10
    SortField: Optional[str] = None
    SortDir: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)