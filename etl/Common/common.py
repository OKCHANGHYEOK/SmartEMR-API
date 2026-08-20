import asyncio
from etl.Config import settings

async def show_progress(message : str):
    dots = ["", ".", "..", "..."]

    while True:
        for dot in dots:
            print(f"\r{message}{dot}   ", end="", flush=True)
            await asyncio.sleep(0.5)

def get_insurance_type(payTpNm : str):
    return "INS" if payTpNm == "급여" else "NON"            

def get_surgery_type(soprTpNm : str):
    return "SUG" if soprTpNm == "수술" else "NON"

def get_sugac_cd(SUGA_Name : str):
    for keyword in settings.category_etc_keyword:
        if keyword in SUGA_Name:
            return "ETC"

    if "진찰료" in SUGA_Name:
        return "ASM"

    if "시술" in SUGA_Name:
        return "PSC"
    
    if "수술" in SUGA_Name:
        return "PSC"

    if "처치" in SUGA_Name:
        return "TRT"

    if "검사" in SUGA_Name:
        return "EXM"

    if "진단서" in SUGA_Name:
        return "DOC"

    if "소견서" in SUGA_Name:
        return "DOC"

    return "ETC"

def get_suga_isUse(SUGA_Name : str) -> bool:
    for keyword in settings.enclude_keyword:
        if keyword in SUGA_Name:
            return True

    for keyword in settings.exclude_keyword:
        if keyword in SUGA_Name:
            return False

    return True        