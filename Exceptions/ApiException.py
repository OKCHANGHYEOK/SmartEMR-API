from fastapi import HTTPException
from Common.Enums import eResponseCode

class ApiException(HTTPException):
    def __init__(
            self, 
            msg: str = "", 
            status_code: int = 400, 
            res_code: eResponseCode = eResponseCode.INTERNAL_SERVER_ERROR
        ):
        super().__init__(status_code=status_code, detail=msg)
        
        self.message = msg
        self.responseCode = res_code