from Exceptions.ApiException import ApiException
from Schemas.MemberDTO import Member_Req, Member_Res
from Schemas.DataResponse import DataResponse
from Entities.Member import Member
from Common import eSP
from .BaseService import BaseSerivce

class MemberService(BaseSerivce):
    async def GetMember(self, request : Member_Req):
        ## 로그인 유저 체크 로직 추후 구현
        
        print(request.keyword)

        item : Member = Member()
        item.MEM_Idx = request.MEM_Idx
        item.MEM_Name = request.MEM_Name
        item.MEM_OperationStatus = request.MEM_OperationStatus
        
        item.sStartDay = request.sStartDay
        item.eStartDay = request.eStartDay
        item.sEndDay = request.sEndDay
        item.eEndDay= request.eEndDay

        item.keyword = request.keyword
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        item.SortField = request.SortField
        item.SortDir = request.SortDir

        ret = await self.DbContext.GetItems(eSP.proc_Member_GetMember, item)

        if ret is None or self.DbContext.retIsSuccess == False:
            raise ApiException(self.DbContext)

        return DataResponse[Member_Res].CreateJsonResult(items=ret, message=self.DbContext.retMessage, isSuccess=True)     
