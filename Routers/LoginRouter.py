from fastapi import Depends
from .BaseRouter import router
from Services.Authentication import LoginService
from Schemas.MemberUserDTO import MemberUser_Req

class LoginRouter():
    @router.post("/login")
    async def login(request : MemberUser_Req,
                    service : LoginService = Depends(LoginService)):
        return await service.login(request)
    
    @router.post("/GetHashPassword")
    async def GetHashPassword(request : MemberUser_Req,
                              service : LoginService = Depends(LoginService)):
        return await service.GetHashedPassWord(request)