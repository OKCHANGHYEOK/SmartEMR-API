from Factory.BaseFactory import BaseFactory
from Schemas.InsuranceDTO import Insurance_Req
from Entities.Insurance import Insurance

class InsuranceFactory(BaseFactory):
    def create(parameter : Insurance_Req) -> Insurance:
        item : Insurance = Insurance()
        item.MEM_Idx = parameter.MEM_Idx
        item.IRC_Idx = parameter.IRC_Idx
        item.PAT_Idx = parameter.PAT_Idx
        item.IRC_Type = parameter.IRC_Type
        item.IRC_CertNum = parameter.IRC_CertNum
        item.IRC_ContractorName = parameter.IRC_ContractorName
        item.IRC_InsuredName = parameter.IRC_InsuredName
        item.IRC_CoName = parameter.IRC_CoName
        item.IRC_Specific = parameter.IRC_Specific
        item.IRC_EffectiveYYMMDD = parameter.IRC_EffectiveYYMMDD    

        return item  