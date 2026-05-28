from fastapi import Depends
from datetime import datetime, timedelta, timezone
from Config import settings
from Exceptions.ApiException import ApiException
from Services.Domain import BaseService
from Schemas.DataResponse import DataResponse
from Schemas.TokenDTO import Token_Req, Token_Res
from Common.eSP import eSP

class TokenService(BaseService):
    async def GetRefreshToken(self, request : Token_Req):
        item : Token_Req = Token_Req()

        item.MUR_Idx = request.MUR_Idx
        item.TOKEN_VALUE = request.TOKEN_VALUE

        ret = await self.DbContext.GetItems(eSP.proc_RefreshToken_GetRefreshToken, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            return None
        
        return DataResponse[Token_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)
    
    async def SetRefreshToken(self, request : Token_Req):
        item : Token_Req = Token_Req()

        item.RTK_Idx = request.RTK_Idx
        item.MUR_Idx = request.MUR_Idx
        item.TOKEN_VALUE = request.TOKEN_VALUE
        item.EXPIRE_DATE = datetime.now(timezone.utc) + timedelta(days=settings.jwt.refresh_token_expire_days)
        item.ISREVOKED = request.ISREVOKED

        ret = await self.DbContext.GetItems(eSP.proc_RefreshToken_SetRefreshToken, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            return None
        
        return DataResponse[Token_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)
    
