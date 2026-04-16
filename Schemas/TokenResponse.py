from typing import Optional
from pydantic import BaseModel

class TokenResponse(BaseModel):
    AccessToken : Optional[str] = ""
    TokenType : Optional[str] = ""
    ExpireMinutes : Optional[float] = 120