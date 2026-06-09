from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TokenDTO(BaseModel):
    RTK_Idx : Optional[int] = None
    MUR_Idx : Optional[int] = None
    TOKEN_VALUE : Optional[str] = None
    ISREVOKED : Optional[bool] = None
    EXPIRE_DATE : Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True, extra="ignore")

class Token_Req(TokenDTO):
    pass

class Token_Res(TokenDTO):
    pass