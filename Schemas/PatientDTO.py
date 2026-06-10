import base64
from .BaseDTO import BaseDTO
from typing import Optional
from datetime import datetime
from pydantic import field_serializer

class PatientDTO(BaseDTO):
    PAT_Idx: Optional[int] = None
    MEM_Idx: Optional[int] = None
    MUR_Idx: Optional[int] = None
    MUR_Idx_DOC: Optional[int] = None
    MUR_Idx_STF: Optional[int] = None
    PAT_BloodType: Optional[str] = None
    PAT_SourceType: Optional[str] = None
    PAT_Name: Optional[str] = None
    PAT_ChartNo: Optional[str] = None
    PAT_Sex: Optional[str] = None
    PAT_Age: Optional[int] = None
    PAT_BirthYear: Optional[str] = None
    PAT_BirthMonth: Optional[str] = None
    PAT_BirthDay: Optional[str] = None
    PAT_RegisterNum1: Optional[str] = None
    PAT_RegisterNum2: Optional[str] = None
    PAT_Hpp1: Optional[str] = None
    PAT_Hpp2: Optional[str] = None
    PAT_Hpp3: Optional[str] = None
    PAT_Address1: Optional[str] = None
    PAT_Address2: Optional[str] = None
    PAT_Address3: Optional[str] = None
    PAT_Email: Optional[str] = None
    PAT_FirstVisitDate: Optional[str] = None
    PAT_LastVisitDate: Optional[str] = None
    PAT_Bigo : Optional[str] = None
    PAT_IsSolar: Optional[str] = None
    PAT_IsAgreePersonalInfo: Optional[str] = None
    PAT_IsForeign: Optional[str] = None
    PAT_IsSMS: Optional[str] = None
    PAT_IsEmail: Optional[str] = None
    PAT_ImageSource: Optional[bytes] = None  # varbinary(MAX) 대응
    PAT_Date: Optional[str] = None
    PAT_YYMMDD: Optional[str] = None
    PAT_IsValid: Optional[bool] = None        # bit 대응

    @field_serializer('PAT_ImageSource')
    def serialize_image(self, v):
        if isinstance(v, bytes):
            return base64.b64encode(v).decode('utf-8')
        return v

class Patient_Req(PatientDTO):
    pass

class Patient_Res(PatientDTO):
    pass   