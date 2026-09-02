from enum import Enum

class eSP(Enum):
    proc_CommonCode_GetCommonCode = 0

    proc_Consultation_GetConsultation = 1
    proc_Consultation_GetConsultationByRCP = 2
    proc_Consultation_SetConsultation = 3
    proc_Consultation_SetConsultationByIRC = 4

    proc_ConsultationOrder_GetConsultationOrder = 5
    proc_ConsultationOrder_SetConsultationOrder = 6 
    proc_ConsultationOrder_SetConsultationOrderProperty = 7

    proc_Insurance_GetInsurance = 8
    proc_Insurance_GetRecentInsurance = 9
    proc_Insurance_SetInsurance = 10

    proc_Member_GetMember = 11
    proc_Member_SetMember = 12

    proc_MemberUser_GetMemberUser = 13
    proc_MemberUser_GetMemberUserForLogin = 14
    proc_MemberUser_SetMemberUser = 15

    proc_Patient_GetPatient = 16
    proc_Patient_SetPatient = 17

    proc_Pay_GetPay = 18
    proc_Pay_SetPay = 19

    proc_Reception_CancelReception = 20
    proc_Reception_GetReception = 21
    proc_Reception_GetReceptionBoard = 22
    proc_Reception_SetReception = 23
    proc_Reception_SetReceptionByIRC = 24
    proc_Reception_SetReceptionByRES = 25

    proc_RefreshToken_GetRefreshToken = 26
    proc_RefreshToken_SetRefreshToken = 27

    proc_Reservation_GetReservation = 28
    proc_Reservation_MoveReservationDate = 29
    proc_Reservation_SetReservation = 30
    proc_Reservation_SetReservationByStatus = 31

    proc_Suga_GetSuga = 32
    proc_Suga_SetSuga = 33
    proc_Suga_SetSugaProperty = 34

    proc_Order_GetOrder = 35