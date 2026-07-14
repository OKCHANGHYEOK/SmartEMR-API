from fastapi import Depends
from .BaseRouter import router
from Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from Schemas.DataResponse import DataResponse
from Services.Domain import MemberUserService

class MemberUserRouter():
    @router.post("/GetMemberUser", response_model=DataResponse[MemberUser_Res])
    async def GetMemberUser(request: MemberUser_Req, service : MemberUserService = Depends(MemberUserService)):
        return await service.GetMemberUser(request)

    @router.post("/SetMemberUser", response_model=DataResponse[MemberUser_Res])
    async def SetMemberUser(request : MemberUser_Req, service : MemberUserService = Depends(MemberUserService)):
        return await service.SetMemberUser(request)