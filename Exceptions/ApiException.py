from fastapi import HTTPException
from Schemas.DataResponse import DataResponse
from typing import TypeVar

T = TypeVar("T")

class ApiException(HTTPException):
    def __init__(self, response : DataResponse[T]):
        self.response = response
        