from fastapi import FastAPI, Depends, HTTPException
from Common import eSP
from Infrastructure import AppDBContext
from Entities.ChartCommonCode import ChartCommonCode_Req  # 요청/결과용 엔티티 클래스

app = FastAPI()

# DbContext 인스턴스 생성 (싱글톤 형태 혹은 필요 시 매번 생성)
appDBContext = AppDBContext()

# @app.get("/api/v1/common-codes/{group_cd}")
# async def GetChartCommonCode(group_cd: str):
#     request_obj = ChartCommonCode_Req(GroupCd=group_cd)
    
#     try:
#         results = await appDBContext.GetItems(eSP.proc_ChartCommonCode_GetChartCommonCode, request_obj)
        
#         if not appDBContext.retIsSuccess:
#             raise HTTPException(status_code=500, detail=appDBContext.retMessage)
            
#         return results
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))