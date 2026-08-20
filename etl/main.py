import asyncio
from etl.Config import settings
from etl.Client.HiraClient import HiraClient
from etl.Common import mapper, parser
from etl.Models.Hira import HiraRequest
from etl.Models.Suga import Suga
from app.Common.eSP import eSP
from app.Infrastructure.AppDBContext import AppDBContext
from datetime import datetime
from tqdm import tqdm

dbcontext = AppDBContext()

async def main():
    print("====e============================")
    print(" SmartEMR API - ETL")
    print("================================")
    print()

    search_result = ""
    parse_result : list | None = None

    while True:
        print("0. 전체 수가 업데이트")
        print("1. 수가 데이터 조회")
        print("2. 수가 데이터 적재")
        print("-1. 종료")
        # print("-1. 수가 데이터 변환 테스트")

        command = input("\n선택 > ")

        if command == "0":
            await update_suga_all()

        if command == "1":
            search_result = await search()

        elif command == "2":
            if await load(search_result, parse_result):
                break

        elif command == "-1":
            break

        else:
            print("잘못된 입력입니다.")

        print()

async def update_suga_all():
    print("전체 수가 업데이트를 진행합니다.")

    client = HiraClient(settings.service_key)
    total_count = 0

    for prefix in tqdm("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "수가 데이터 업데이트"):
        req = HiraRequest()
        req.fee_code = f"{prefix}%"
        req.numOfRows = 10000

        result = await client.get_mdfee_list(req)

        if not result:
            print("조회된 결과가 없습니다.")
            continue

        parsed = parser.convert_from_xml(result)

        if not parsed:
            print("데이터 변환 실패하였습니다.")
            continue

        mapped : list[Suga] = mapper.mapping_suga(parsed)

        suga_property = ""

        for suga in mapped:
            suga_property += "$" if len(suga_property) > 0 else ""
            suga_property += suga.SUGA_Code + "|"
            suga_property += suga.SUGA_ClassCode + "|"
            suga_property += suga.SUGA_InsuranceType + "|"
            suga_property += suga.SUGA_SugeryType + "|"
            suga_property += suga.SUGAC_Cd + "|"
            suga_property += suga.SUGAG_Cd if suga.SUGAG_Cd else "" + "|"
            suga_property += suga.SUGAI_Cd if  suga.SUGAI_Cd else "" + "|"
            suga_property += suga.SUGA_Name + "|"
            suga_property += suga.SUGA_ClinicPrice + "|"
            suga_property += suga.SUGA_HospitalPrice + "|"
            suga_property += suga.SUGA_DentistPrice + "|"
            suga_property += suga.SUGA_HealthPrice + "|"
            suga_property += suga.SUGA_BirthCenterPrice + "|"
            suga_property += suga.SUGA_KorMedicinePrice + "|"
            suga_property += suga.SUGA_EffectiveFromDay + "|"
            suga_property += suga.SUGA_EffectiveToDay.strftime('%Y-%m-%d') + "|"
            suga_property += "True" if suga.SUGA_IsUse else "False" + "|"

        setSuga = Suga()
        setSuga.SUGA_Property = suga_property

        ret : list[Suga] = dbcontext.GetItems[Suga](eSP.proc_Suga_SetSugaProperty, setSuga)

        if not ret or dbcontext.retIsSuccess == False:
            print("수가 데이터를 저장하지 못했습니다.")
            continue

        total_count += len(ret)

    print(f"총 {total_count}건의 수가를 업데이트 완료했습니다.")

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
        request.numOfRows = 10000

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

async def load(search_result : str, parse_result : list) -> bool:
    target_data = []

    if not search_result and not parse_result:
        print("적재할 데이터가 없습니다.")
        return False

    print("수가 데이터 적재를 진행합니다.")

    if search_result:
        print("데이터 변환중...")

        source_data = parser.convert_from_xml(search_result)

        for item in tqdm(source_data, desc="수가 데이터 변환"):
            target_data = mapper.mapping_suga(item)

        print("데이터 변환 완료.")
        
    elif parse_result:
        target_data = parse_result

    if not target_data:
        print("작업 진행 중 문제가 발생했습니다. 다시 시도해주세요.")
        return False

    print(target_data)

    # print("DB 에 데이터를 적재합니다.")

    # for item in tqdm(target_data, desc="수가 데이터 DB적재"):
    #     await dbcontext.GetItem[Suga](eSP.proc_Suga_SetSuga, item)

    # print("데이터 적재가 완료되었습니다.")

    return True           

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