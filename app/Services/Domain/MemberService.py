from app.Exceptions.ApiException import ApiException
from app.Schemas.MemberDTO import Member_Req, Member_Res
from app.Schemas.DataResponse import DataResponse
from app.Entities.Member import Member
from app.Common import eSP
from .BaseService import BaseService

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