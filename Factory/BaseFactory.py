from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from Schemas.BaseDTO import BaseDTO
from Entities.BaseEntity import BaseEntity

TReq = TypeVar("TReq", bound=BaseDTO)
TRes = TypeVar("TRes", bound=BaseEntity)

class BaseFactory():
    @abstractmethod
    def create(parameter : TReq) -> TRes:
        pass