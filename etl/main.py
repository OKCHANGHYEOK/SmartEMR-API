import asyncio
from etl.Common import parser
from etl.Config import settings
from etl.Client.HiraClient import HiraClient
from etl.Models.Hira import HiraRequest
from etl.Models.Suga import Suga

async def main():
    print("====e============================")
    print(" SmartEMR API - ETL")
    print("================================")
    print()

    search_result = ""
    parse_result : list | None = None

    while True:
        print("1. 수가 데이터 조회")
        print("2. 수가 데이터 적재")
        print("0. 종료")
        print("-1. 수가 데이터 변환 테스트")

        command = input("\n선택 > ")

        if command == "1":
            search_result = await search()

        elif command == "2":
            await load(search_result, parse_result)

        elif command == "0":
            break

        elif command == "-1":
            parse_result = await test_parser()

        else:
            print("잘못된 입력입니다.")

        print()

async def search():
    from etl.Common.common import show_progress

    hira_client = HiraClient(settings.service_key)

    while True:
        print("수가 데이터를 조회합니다.")
        print("수가코드/분류번호/수가명으로 검색하세요. 각 검색어는 '/' 로 구분합니다.")

        keyword = input(">> ")

        params = [param.strip() for param in keyword.split("/")]

        if all(not param for param in params):
            print("검색 조건이 올바르지 않습니다. 다시 입력해주세요.")
            continue

        request = HiraRequest()
        request.fee_code = params[0]
        request.div_no = params[1] if len(params) >= 2 else ''
        request.kor_name = params[2] if len(params) >= 3 else ''

        search_task = asyncio.create_task(show_progress("데이터를 조회하고 있습니다."))

        try:
            response = await hira_client.get_mdfee_list(request)

        finally:
            search_task.cancel()
            print("\r" + " " * 40 + "\r", end="", flush=True)

        if not response:
            print("수가 조회에 실패했습니다.")
            continue    

        print(response)        
        print("조회 완료되었습니다. 데이터 적재를 진행하시려면 엔터키를 입력하세요.")

        command = input("")

        if command == "":
            return response        
        else:
            continue

async def load(search_result : str, parse_result : list):
    from etl.Common import mapper, parser
    from tqdm import tqdm

    if not search_result and not parse_result:
        print("적재할 데이터가 없습니다.")
        return

    print("수가 데이터 적재를 진행합니다.")

    if search_result:
        print("데이터 변환중...")

        data = parser.convert_from_xml(search_result)

        for item in tqdm(data, desc="수가 데이터 변환"):
            result = mapper.mapping_suga(item)

        print("데이터 변환 완료.")
        
    elif parse_result:
        print(parse_result)

async def test_parser() -> list[Suga]:
    from etl.Common import mapper, parser
    from tqdm import tqdm
    from pathlib import Path

    print("수가 데이터 변환 테스트를 진행합니다.")
    print("0. 진찰료")
    print("1. 시술")
    print("2. 처치")
    print("3. 검사")
    print("4. 문서 - 진단서")
    print("5. 문서 - 소견서")
    print("-1. 메인메뉴로")

    command = input("\n선택 > ")

    base_file_dir = "etl/Data/Order/Raws"
    target_code = ""

    match command:
        case "0": 
            target_code = "asm"
        case "1":
            target_code = "psc"
        case "2":
            target_code = "trt"
        case "3":
            target_code = "exm"
        case "4":
            target_code = "doc_diagnosis"
        case "5":
            target_code = "doc_opinion"
        case "-1":
            return    

    target_file_name = f"{base_file_dir}/hira_mdfee_{target_code}.xml"                           

    with open(target_file_name, "r", encoding="utf-8") as f:
        xml = f.read()

    data = parser.convert_from_xml(xml)

    for item in tqdm(data, desc="수가 데이터 변환 테스트"):
       result = mapper.mapping_suga(data)

    print("데이터 변환 완료")

    return result       

if __name__ == "__main__":
    asyncio.run(main())