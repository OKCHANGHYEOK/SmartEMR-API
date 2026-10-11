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

    proc_EmailVerification_GetEmailVerification = 10
    proc_EmailVerification_SetEmailVerification = 11

    proc_Insurance_GetInsurance = 12
    proc_Insurance_GetRecentInsurance = 13
    proc_Insurance_SetInsurance = 14

    proc_Member_GetMember = 15
    proc_Member_SetMember = 16

    proc_MemberUser_GetMemberUser = 17
    proc_MemberUser_GetMemberUserForLogin = 18
    proc_MemberUser_SetMemberUser = 19

    proc_Patient_GetPatient = 20
    proc_Patient_SetPatient = 21

    proc_Pay_GetPay = 22
    proc_Pay_SetPay = 23
    proc_Pay_CancelPay = 24
    proc_Pay_UpdatePayByPrice = 25

    proc_PayItem_GetPayItem = 26
    proc_PayItem_SetPayItem = 27

    proc_Reception_CancelReception = 28
    proc_Reception_GetReception = 29
    proc_Reception_GetReceptionBoard = 30
    proc_Reception_SetReception = 31
    proc_Reception_SetReceptionByIRC = 32
    proc_Reception_SetReceptionByRES = 33

    proc_RefreshToken_GetRefreshToken = 34
    proc_RefreshToken_SetRefreshToken = 35

    proc_Reservation_GetReservation = 36
    proc_Reservation_MoveReservationDate = 37
    proc_Reservation_SetReservation = 38
    proc_Reservation_SetReservationByStatus = 39

    proc_Suga_GetSuga = 40
    proc_Suga_SetSuga = 41
    proc_Suga_SetSugaProperty = 42

    proc_Order_GetOrder = 43
    
    proc_NaverPay_SetNaverPay = 44