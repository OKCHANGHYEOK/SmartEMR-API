from fastapi import APIRouter, Depends
from app.Schemas.MemberDTO import Member_Req, Member_Res
from app.Schemas.DataResponse import DataResponse
from app.Services.Domain import MemberService
from app.Services.Authentication.AuthenticateService import AuthenticateService

router = APIRouter()

class MemberRouter():    
    @router.post("/GetMember", response_model=DataResponse[Member_Res])
    async def GetMember(request : Member_Req, 
                        service : MemberService = Depends(MemberService)):
        return await service.GetMember(request)
        
    @router.post("/SetMember", response_model=DataResponse[Member_Res], dependencies=[Depends(AuthenticateService.verify_jwt_token)])
    async def SetMember(request : Member_Req,
                        serivce : MemberService = Depends(MemberService)):
        return await serivce.SetMember(request)
        