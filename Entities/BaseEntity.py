from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseEntity(Base):
    __abstract__ = True

    sDay = Column(String(10))
    eDay =Column(String(10))
    keyword = Column(String(500))
    PageIndex = Column(Integer)
    PageSize = Column(Integer, default=10)
    SortField = Column(String(50))
    SortDir = Column(String(50))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # 클래스에 해당 속성이 정의되어 있는 경우에만 값을 넣어줍니다.
            if hasattr(self, key):
                setattr(self, key, value)
        # 정의되지 않은 나머지 값들은 자동으로 무시됩니다.
    # ------------------