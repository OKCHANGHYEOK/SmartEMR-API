from enum import Enum

class eSP(Enum):
    proc_CommonCode_GetCommonCode = 0

    proc_Consultation_GetConsultation = 1
    proc_Consultation_GetConsultationByRCP = 2
    proc_Consultation_SetConsultation = 3

    proc_ConsultationOrder_GetConsultationOrder = 4
    proc_ConsultationOrder_SetConsultationOrder = 5 
    proc_ConsultationOrder_SetConsultationOrderProperty = 6

    proc_Insurance_GetInsurance = 7
    proc_Insurance_GetRecentInsurance = 8
    proc_Insurance_SetInsurance = 9

    proc_Member_GetMember = 10
    proc_Member_SetMember = 11

    proc_MemberUser_GetMemberUser = 12
    proc_MemberUser_GetMemberUserForLogin = 13
    proc_MemberUser_SetMemberUser = 14

    proc_Patient_GetPatient = 15
    proc_Patient_SetPatient = 16

    proc_Pay_GetPay = 17
    proc_Pay_SetPay = 18

    proc_Reception_CancelReception = 19
    proc_Reception_GetReception = 20
    proc_Reception_GetReceptionBoard = 21
    proc_Reception_SetReception = 22
    proc_Reception_SetReceptionByIRC = 23
    proc_Reception_SetReceptionByRES = 24

    proc_RefreshToken_GetRefreshToken = 25
    proc_RefreshToken_SetRefreshToken = 26

    proc_Reservation_GetReservation = 27
    proc_Reservation_MoveReservationDate = 28
    proc_Reservation_SetReservation = 29
    proc_Reservation_SetReservationByStatus = 30

    proc_Suga_GetSuga = 31
    proc_Suga_SetSuga = 32
    proc_Suga_SetSugaProperty = 33

    proc_Order_GetOrder = 34