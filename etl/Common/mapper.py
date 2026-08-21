from etl.Models.Suga import Suga
from datetime import datetime
from etl.Common import common

def mapping_suga(dict_data : dict) -> list[dict]:
    suga_items = []

    for key in dict_data:
        body = dict_data[key].get("body")

        if not body:
            continue

        items = body.get("items")

        for item in items:
            data = items.get(item)

            for suga_source in data:
                suga_items.append(convert_to_suga(suga_source))

    return suga_items

def convert_to_suga(suga_source : dict) -> dict:
    SUGA_Name   = suga_source.get("korNm")

    item = {
        'SUGA_Name' : suga_source.get("korNm"),
        'SUGA_Code' : suga_source.get("mdfeeCd"),
        'SUGA_ClassCode' : suga_source.get("mdfeeDivNo"),
        'SUGA_InsuranceType' : common.get_insurance_type(suga_source.get("payTpCd")),
        'SUGA_SurgeryType' : common.get_surgery_type(suga_source.get("soprTpNm")),
        'SUGAC_Cd' : common.get_sugac_cd(SUGA_Name),
        'SUGAG_Cd' : '',
        'SUGAI_Cd' : '', 
        'SUGA_Price' : suga_source.get("unprc2"),           # 병원급 수가를 기준으로함에 따른 설정
        'SUGA_ClinicPrice' : suga_source.get("unprc1"),
        'SUGA_HospitalPrice' : suga_source.get("unprc2"),
        'SUGA_DentistPrice' : suga_source.get("unprc3"),
        'SUGA_HealthPrice' : suga_source.get("unprc4"),
        'SUGA_BirthCenterPrice' : suga_source.get("unprc5"),
        'SUGA_KorMedicinePrice' : suga_source.get("unprc6"),
        'SUGA_EffectiveFromDay' : suga_source.get("adtStaDd"),
        'SUGA_EffectiveToDay' : datetime(year=2999, month=12, day=31).strftime('%Y-%m-%d'),
        'SUGA_IsUse' : common.get_suga_isUse(SUGA_Name)
    }

    return item