from pydantic import BaseModel
from typing import Optional

class BaseDTO(BaseModel):
    # API 요청 시 공통으로 들어오는 페이징/검색 필드
    sDay: Optional[str] = None
    eDay: Optional[str] = None
    keyword: Optional[str] = None
    PageIndex: int = 1
    PageSize: int = 10
    SortField: Optional[str] = None
    SortDir: Optional[str] = None

    class Config:
        # 이 설정이 있으면 SQLAlchemy 객체를 Pydantic으로 자동 변환해줍니다.
        from_attributes = True