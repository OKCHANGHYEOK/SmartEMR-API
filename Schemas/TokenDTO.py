from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TokenDTO(BaseModel):
    MUR_Idx : Optional[int] = None
    TOKEN_VALUE : Optional[str] = None

    model_config = ConfigDict(from_attributes=True, extra="ignore")

class Token_Req(TokenDTO):
    pass

class Token_Res(TokenDTO):
    RTK_Idx : Optional[int] = None
    EXPIRE_DATE : Optional[datetime] = None
    ISREVOKED : Optional[bool] = None

    