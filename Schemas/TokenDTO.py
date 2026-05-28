from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class TokenDTO(BaseModel):
    RTK_Idx : Optional[int] = None
    MUR_Idx : Optional[int] = None
    TOKEN_VALUE : Optional[str] = None
    EXPIRE_DATE : Optional[datetime] = None
    ISREVOKED : Optional[bool] = None

    model_config = ConfigDict(from_attributes=True, extra="allow")

class Token_Req(TokenDTO):
    pass

class Token_Res(TokenDTO):
    pass   