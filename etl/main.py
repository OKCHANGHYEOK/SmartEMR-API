import asyncio
from etl.Config import settings
from etl.Client.HiraClient import HiraClient, HiraRequest

async def main():
    client = HiraClient(settings.service_key)

    req = HiraRequest()
    req.fee_code = "NA242W"

    result = await client.get_mdfee_list(req)

    print(result)

if __name__ == "__main__":
    asyncio.run(main())