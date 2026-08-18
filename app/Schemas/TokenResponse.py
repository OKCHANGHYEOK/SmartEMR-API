from typing import Optional
from pydantic import BaseModel
from app.Schemas.MemberDTO import Member_Res
from app.Schemas.MemberUserDTO import MemberUser_Res

class TokenResponse(BaseModel):
    AccessToken : Optional[str] = ""
    RefreshToken : Optional[str] = ""
    TokenType : Optional[str] = ""
    ExpireMinutes : Optional[float] = 120
    Member : Optional[Member_Res] = None
    User : Optional[MemberUser_Res] = None