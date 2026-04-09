from fastapi import APIRouter, Depends
from Schemas.MemberDTO import Member_Req, Member_Res
from Schemas.DataResponse import DataResponse
from Services.Domain import MemberService
from Dependencies.dependencies import ServiceProvider

router = APIRouter()

class MemberRouter():
    @router.post("/GetMember", response_model=DataResponse[Member_Res])
    async def GetMember(request : Member_Req, 
                        service : MemberService = Depends(ServiceProvider(MemberService))):
        return await service.GetMember(request)
        
