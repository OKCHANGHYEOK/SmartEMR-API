from fastapi import APIRouter, Depends
from app.Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from app.Schemas.DataResponse import DataResponse
from app.Services.Authentication.AuthenticateService import AuthenticateService
from app.Services.Domain import MemberUserService

router = APIRouter()

class MemberUserRouter():
    @router.post("/GetMemberUserByCheckDuplicateId", response_model=DataResponse[MemberUser_Res])
    async def GetMemberUserByCheckDuplicateId(request : MemberUser_Req, service : MemberUserService = Depends(MemberUserService)):
        return await service.GetMemberUserByCheckDuplicateId(request)
    
    @router.post("/GetMemberUser", response_model=DataResponse[MemberUser_Res], dependencies=[Depends(AuthenticateService.verify_jwt_token)])
    async def GetMemberUser(request: MemberUser_Req, service : MemberUserService = Depends(MemberUserService)):
        return await service.GetMemberUser(request)

    @router.post("/SetMemberUser", response_model=DataResponse[MemberUser_Res], dependencies=[Depends(AuthenticateService.verify_jwt_token)])
    async def SetMemberUser(request : MemberUser_Req, service : MemberUserService = Depends(MemberUserService)):
        return await service.SetMemberUser(request)