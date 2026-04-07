from Entities.Member import Member, Member_Req, Member_Res
from Entities.DataResponse import DataResponse
from Common import eSP
from .BaseService import BaseSerivce

class MemberService(BaseSerivce):
    async def GetMember(self, request : Member_Req):
        ## 로그인 유저 체크 로직 추후 구현
        
        item = Member()
        item.MEM_Idx = request.MEM_Idx
        item.MEM_Name = request.MEM_Name
        item.MEM_OperationStatus = request.MEM_OperationStatus
        item.sDay = request.sDay
        item.eDay = request.eDay

        item.keyword = request.keyword
        item.PageSize = request.PageSize
        item.PageIndex = request.PageIndex
        item.SortField = request.SortField
        item.SortDir = request.SortDir

        ret : DataResponse[Member_Res] = await self.dbContext.GetItems(eSP.proc_Member_GetMember, item)

        if ret is None or ret.IsSuccess == False:
            ## API예외 발생키기기

                
            return None

        ## JSON 응답 본문 반환        
