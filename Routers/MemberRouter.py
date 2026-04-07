from fastapi import APIRouter, Depends
from Entities.Member import Member_Req
from Services import MemberService

router = APIRouter()

class MemberRouter():
    @router.get("/GetMember")
    async def GetMember(self, request : Member_Req):
        return MemberService.GetMember(request)
        
