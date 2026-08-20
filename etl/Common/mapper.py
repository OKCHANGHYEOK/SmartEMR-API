from etl.Models.Suga import Suga
from datetime import datetime
from etl.Common import common

def mapping_suga(dict_data : dict) -> list:
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

def convert_to_suga(suga_source : dict) -> Suga:
    item : Suga = Suga()
    item.SUGA_Name = suga_source.get("korNm")
    item.SUGA_Code = suga_source.get("mdfeeCd")
    item.SUGA_ClassCode = suga_source.get("mdfeeDivNo")
    item.SUGA_InsuranceType = common.get_insurance_type(suga_source.get("payTpNm"))
    item.SUGA_SugeryType = common.get_sugery_type(suga_source.get("soprTpNm"))
    item.SUGAC_Cd = common.get_sugac_cd(item.SUGA_Name)
    item.SUGA_Price = suga_source.get("unprc")
    item.SUGA_ClinicPrice = suga_source.get("unprc1")
    item.SUGA_HospitalPrice = suga_source.get("unprc2")
    item.SUGA_DentistPrice = suga_source.get("unprc3")
    item.SUGA_HealthPrice = suga_source.get("unprc4")
    item.SUGA_BirthCenterPrice = suga_source.get("unprc5")
    item.SUGA_KorMedicinePrice = suga_source.get("unprc6")
    item.SUGA_EffectiveFromDay = suga_source.get("adtStaDd")
    item.SUGA_EffectiveToDay = datetime(year=2999, month=12, day=31)
    item.SUGA_IsUse = common.get_suga_isUse(item.SUGA_Name)

    return item