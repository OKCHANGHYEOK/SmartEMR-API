from fastapi import APIRouter, Depends
from Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from Schemas.DataResponse import DataResponse
from Services.Domain import MemberUserService
from Dependencies.dependencies import ServiceProvider

router = APIRouter()

class MemberUserRouter():
    @router.post("/SetMemberUser", response_model=DataResponse[MemberUser_Res])
    async def SetMemberUser(request : MemberUser_Req,
                            service : MemberUserService = Depends(ServiceProvider(MemberUserService))):
        return await service.SetMemberUser(request)