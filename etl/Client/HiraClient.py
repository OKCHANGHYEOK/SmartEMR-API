import httpx
from etl.Config import settings

class HiraClient:
    base_url = settings.api_url

    def __init__(self, service_key : str):
        self.service_key = service_key

    async def get_mdfee_list(self, request : HiraRequest):
        url = f"{self.base_url}/getDiagnossMdfeeList"
        params = {
            "ServiceKey" : self.service_key,
            "pageNo" : request.pageNo,
            "numOfRows" : request.numOfRows,
            "mdfeeCd" : request.fee_code,
            "mdfeeDivNo" : request.div_no,
            "korNm" : request.kor_name
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            return response.text