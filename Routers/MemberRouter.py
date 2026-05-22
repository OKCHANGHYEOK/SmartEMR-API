from fastapi import APIRouter, Depends
from Schemas.MemberDTO import Member_Req, Member_Res
from Schemas.DataResponse import DataResponse
from Services.Domain import MemberService

router = APIRouter()

class MemberRouter():
    @router.post("/GetMember", response_model=DataResponse[Member_Res])
    async def GetMember(request : Member_Req, 
                        service : MemberService = Depends(MemberService)):
        return await service.GetMember(request)
        
