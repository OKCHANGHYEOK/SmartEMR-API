from enum import Enum

class eSP(Enum):
    proc_CommonCode_GetCommonCode = 0

    proc_Consultation_GetConsultation = 1
    proc_Consultation_GetConsultationByRCP = 2
    proc_Consultation_SetConsultation = 3
    proc_Consultation_SetConsultationByIRC = 4
    proc_Consultation_SetConsultationByPAY = 5

    proc_ConsultationOrder_GetConsultationOrder = 6
    proc_ConsultationOrder_SetConsultationOrder = 7 
    proc_ConsultationOrder_SetConsultationOrderProperty = 8

    proc_Insurance_GetInsurance = 9
    proc_Insurance_GetRecentInsurance = 10
    proc_Insurance_SetInsurance = 11

    proc_Member_GetMember = 12
    proc_Member_SetMember = 13

    proc_MemberUser_GetMemberUser = 14
    proc_MemberUser_GetMemberUserForLogin = 15
    proc_MemberUser_SetMemberUser = 16

    proc_Patient_GetPatient = 17
    proc_Patient_SetPatient = 18

    proc_Pay_GetPay = 19
    proc_Pay_SetPay = 20

    proc_Reception_CancelReception = 21
    proc_Reception_GetReception = 22
    proc_Reception_GetReceptionBoard = 23
    proc_Reception_SetReception = 24
    proc_Reception_SetReceptionByIRC = 25
    proc_Reception_SetReceptionByRES = 26

    proc_RefreshToken_GetRefreshToken = 27
    proc_RefreshToken_SetRefreshToken = 28

    proc_Reservation_GetReservation = 29
    proc_Reservation_MoveReservationDate = 30
    proc_Reservation_SetReservation = 31
    proc_Reservation_SetReservationByStatus = 32

    proc_Suga_GetSuga = 33
    proc_Suga_SetSuga = 34
    proc_Suga_SetSugaProperty = 35

    proc_Order_GetOrder = 36