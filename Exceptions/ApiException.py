from fastapi import HTTPException
from Infrastructure import AppDBContext
from Schemas.DataResponse import DataResponse
from typing import TypeVar
from Common.Enums import eResponseCode

T = TypeVar("T")

class ApiException(HTTPException):
    def __init__(self, dbContext : AppDBContext):
        self.response = DataResponse[T](
            IsSuccess=False,
            Message=dbContext.retMessage,
            items = []
        )

    def __init__(self, msg : str = "", res_code : eResponseCode = None):
        self.response = DataResponse[T](
            IsSuccess=False,
            Message=msg,
            ResponseCode=res_code
        )

        