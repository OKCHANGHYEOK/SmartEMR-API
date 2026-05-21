from typing import Optional
from pydantic import BaseModel
from Schemas.MemberDTO import Member_Res
from Schemas.MemberUserDTO import MemberUser_Res

class TokenResponse(BaseModel):
    AccessToken : Optional[str] = ""
    TokenType : Optional[str] = ""
    ExpireMinutes : Optional[float] = 120
    Member : Optional[Member_Res] = None
    User : Optional[MemberUser_Res] = None