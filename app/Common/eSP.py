from enum import Enum

class eSP(Enum):
    proc_CommonCode_GetCommonCode = 0

    proc_Consultation_GetConsultation = 1
    proc_Consultation_GetConsultationByRCP = 2
    proc_Consultation_SetConsultation = 3
    proc_Consultation_CancelConsultation = 4
    proc_Consultation_SetConsultationByIRC = 5
    proc_Consultation_SetConsultationByPAY = 6

    proc_ConsultationOrder_GetConsultationOrder = 7
    proc_ConsultationOrder_SetConsultationOrder = 8
    proc_ConsultationOrder_SetConsultationOrderProperty = 9

    proc_Insurance_GetInsurance = 10
    proc_Insurance_GetRecentInsurance = 11
    proc_Insurance_SetInsurance = 12

    proc_Member_GetMember = 13
    proc_Member_SetMember = 14

    proc_MemberUser_GetMemberUser = 15
    proc_MemberUser_GetMemberUserForLogin = 16
    proc_MemberUser_SetMemberUser = 17

    proc_Patient_GetPatient = 18
    proc_Patient_SetPatient = 19

    proc_Pay_GetPay = 20
    proc_Pay_SetPay = 21

    proc_PayItem_GetPayItem = 22
    proc_PayItem_SetPayItem = 23

    proc_Reception_CancelReception = 24
    proc_Reception_GetReception = 25
    proc_Reception_GetReceptionBoard = 26
    proc_Reception_SetReception = 27
    proc_Reception_SetReceptionByIRC = 28
    proc_Reception_SetReceptionByRES = 29

    proc_RefreshToken_GetRefreshToken = 30
    proc_RefreshToken_SetRefreshToken = 31

    proc_Reservation_GetReservation = 32
    proc_Reservation_MoveReservationDate = 33
    proc_Reservation_SetReservation = 34
    proc_Reservation_SetReservationByStatus = 35

    proc_Suga_GetSuga = 36
    proc_Suga_SetSuga = 37
    proc_Suga_SetSugaProperty = 38

    proc_Order_GetOrder = 39