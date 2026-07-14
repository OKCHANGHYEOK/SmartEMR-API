from fastapi import Depends
from .BaseRouter import router
from Schemas.MemberDTO import Member_Req, Member_Res
from Schemas.DataResponse import DataResponse
from Services.Domain import MemberService

class MemberRouter():
    @router.post("/GetMember", response_model=DataResponse[Member_Res])
    async def GetMember(request : Member_Req, 
                        service : MemberService = Depends(MemberService)):
        return await service.GetMember(request)
        
