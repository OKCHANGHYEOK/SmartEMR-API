class HiraRequest:
    pageNo : int
    numOfRows : int 
    fee_code : str
    div_no : str 
    kor_name : str

    def __init__(self, pageNo : int = 1, numOfRows : int = 100, fee_code : str = "", div_no : str = "", kor_name : str = ""):
        self.pageNo = pageNo
        self.numOfRows = numOfRows
        self.fee_code = fee_code
        self.div_no = div_no
        self.kor_name = kor_name

class HiraResponse:
    adtStaDd : str          # 적용시작일자
    cvalPnt : int           # 상대가치점수 ( 미사용 ) 
    essSelPayDpApvYn : str  # 필수선별급여중복인정여부 ( y/n 미사용 )
    korNm : str             # 한글명
    mdfeeCd : str           # 수가코드
    mdfeeDivNo : str        # 수가분류번호
    payTpCd : str           # 급여구분명 ( 급여/ 비급여 )
    slfBrdnRtCzaApvYn : str # 본인부담율A항 인정여부 ( y/n 미사용 )
    slfBrdnRtCzbApvYn : str # 본인부담율B항 인정여부 ( y/n 미사용 )
    soprTpNm : str          # 수술구분명 ( 수술/비수술 )
    unprc : int             # 적용단가
    unprc1 : int            # 의원단가
    unprc2 : int            # 병원단가
    unprc3 : int            # 치과병의원단가
    unprc4 : int            # 보건기관단가
    unprc5 : int            # 조산원단가
    unprc6 : int            # 한방병원단가           

    
