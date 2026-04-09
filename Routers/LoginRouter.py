from fastapi import APIRouter, Depends
from Dependencies.dependencies import GetLoginService
from Services.Authentication import LoginService
from Schemas.MemberUserDTO import MemberUser_Req

router = APIRouter()

class LoginRouter():
    @router.post("/login")
    async def login(request : MemberUser_Req,
                    service : LoginService = Depends(GetLoginService)):
        return await service.login(request)
    
    @router.post("/GetHashPassword")
    async def GetHashPassword(request : MemberUser_Req,
                              service : LoginService = Depends(GetLoginService)):
        return await service.GetHashedPassWord(request)