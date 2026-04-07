from fastapi import HTTPException
from Infrastructure import AppDBContext
from Schemas.DataResponse import DataResponse
from typing import TypeVar

T = TypeVar("T")

class ApiException(HTTPException):
    def __init__(self, dbContext : AppDBContext):
        self.response = DataResponse[T](
            IsSuccess=False,
            Message=dbContext.retMessage,
            items = []
        )
        