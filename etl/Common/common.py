import asyncio
import sys

async def show_progress(message : str):
    dots = ["", ".", "..", "..."]

    while True:
        for dot in dots:
            print(f"\r{message}{dot}   ", end="", flush=True)
            await asyncio.sleep(0.5)

def get_insurance_type(payTpNm : str):
    return "INS" if payTpNm == "급여" else "NON"            

def get_sugery_type(soprTpNm : str):
    return "SUG" if soprTpNm == "수술" else "NON"