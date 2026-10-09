from app.Exceptions.ApiException import ApiException
from app.Schemas.MemberDTO import Member_Req, Member_Res
from app.Schemas.MemberUserDTO import MemberUser_Req, MemberUser_Res
from app.Schemas.DataResponse import DataResponse
from app.Entities.Member import Member
from app.Entities.MemberUser import MemberUser
from app.Common import eSP
from app.Services.Domain.BaseService import BaseService
from app.Services.Authentication.HashService import HashService

class MemberService(BaseService):
    async def GetMember(self, request : Member_Req):
        item : Member = Member()
        item.MEM_Idx = request.MEM_Idx
        item.MEM_Name = request.MEM_Name
        item.MEM_OperationStatus = request.MEM_OperationStatus
        item.MEM_Address = request.MEM_Address

        item.sStartDay = request.sStartDay
        item.eStartDay = request.eStartDay
        item.sEndDay = request.sEndDay
        item.eEndDay= request.eEndDay

        item.Keyword = request.Keyword
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        item.SortField = request.SortField
        item.SortDir = request.SortDir

        ret = await self.DbContext.GetItems[Member_Res](eSP.proc_Member_GetMember, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)

        return DataResponse[Member_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage)     

    async def GetMemberByCheckDuplicateMediNo(self, request : Member_Req):
        item : Member = Member()
        
        item.MEM_MediNo = request.MEM_MediNo
        
        ret = await self.DbContext.GetItem[Member](eSP.proc_Member_GetMember, item)
        
        if self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Member_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)

    async def SetMember(self, request : Member_Req):
        item : Member = Member()
        item.MEM_Idx = request.MEM_Idx
        item.MEM_Name = request.MEM_Name
        item.MEM_OperationStatus = request.MEM_OperationStatus
        item.MEM_Address1 = request.MEM_Address1
        item.MEM_Address2 = request.MEM_Address2
        item.MEM_Address3 = request.MEM_Address3
        item.MEM_BizNum = request.MEM_BizNum
        item.MEM_MediNo = request.MEM_MediNo
        item.MEM_Tel1 = request.MEM_Tel1
        item.MEM_Tel2 = request.MEM_Tel2
        item.MEM_Tel3 = request.MEM_Tel3
        item.MEM_IsValid = request.MEM_IsValid
        
        ret = await self.DbContext.GetItem[Member_Res](eSP.proc_Member_SetMember, item)
        
        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext.retMessage)
        
        return DataResponse[Member_Res].CreateJsonResult(item=ret, message=self.DbContext.retMessage)
    
    async def SignUp(self, request : Member_Req) -> DataResponse[Member_Res]:
        if request.MEM_Idx and request.MEM_Idx > 0:
            raise ApiException("올바르지 않은 요청입니다. 기존 의료기관으로 가입하세요.")
                
        async with self.DbContext.AsyncSessionLocal() as session:
            try:
                getMemberByMediNo = Member()
                getMemberByMediNo.MEM_MediNo = request.MEM_MediNo
                
                retMEMByMediNo : Member_Res = await self.DbContext.GetItem[Member_Res](eSP.proc_Member_GetMember, getMemberByMediNo, session) 
        
                if retMEMByMediNo and retMEMByMediNo.MEM_Idx > 0 :
                    raise ApiException("요양기관번호 중복된 회원사가 존재합니다.")                 
                        
                item : Member = Member()
                
                item.MEM_Idx = 0
                item.MEM_Name = request.MEM_Name
                item.MEM_BizType = request.MEM_BizType
                item.MEM_BizNum = request.MEM_BizNum
                item.MEM_MediNo = request.MEM_MediNo
                item.MEM_OperationStatus = 1
                
                retMEM : Member_Res = await self.DbContext.GetItem[Member_Res](eSP.proc_Member_SetMember, item, session)
                
                if not retMEM or self.DbContext.retIsSuccess == False:
                    raise ApiException(self.DbContext.retMessage)
                
                MURItem = request.MURItem
                
                setMUR = MemberUser()
        
                setMUR.MEM_Idx = retMEM.MEM_Idx
                setMUR.MUR_Name = MURItem.MUR_Name
                setMUR.MUR_Id = MURItem.MUR_Id
                setMUR.MUR_PassWord = HashService.HashPassword(MURItem.MUR_PassWord)
                setMUR.MUR_Role = MURItem.MUR_Role if MURItem.MUR_Role else "USR"
                setMUR.MUR_Department = MURItem.MUR_Department
                setMUR.MUR_JobCode = MURItem.MUR_JobCode
                setMUR.MUR_LicenseNo = MURItem.MUR_LicenseNo
                
                retMUR : MemberUser_Res = await self.DbContext.GetItem[MemberUser_Res](eSP.proc_MemberUser_SetMemberUser, setMUR)
                
                if not retMUR or self.DbContext.retIsSuccess == False:
                    raise ApiException(self.DbContext.retMessage)
                
                await session.commit()
            
            except Exception:
                await session.rollback()
                raise        
        
        retMEM.MURItem = retMUR
        
        return DataResponse[Member_Res].CreateJsonResult(item=retMEM, message=self.DbContext.retMessage)            