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
    proc_EmailVerification_GetEmailVerificationByVerify = 11
    proc_EmailVerification_SetEmailVerification = 12

    proc_Insurance_GetInsurance = 13
    proc_Insurance_GetRecentInsurance = 14
    proc_Insurance_SetInsurance = 15

    proc_Member_GetMember = 16
    proc_Member_SetMember = 17

    proc_MemberUser_GetMemberUser = 18
    proc_MemberUser_GetMemberUserForLogin = 19
    proc_MemberUser_SetMemberUser = 20
    proc_MemberUser_ChangePassword = 21

    proc_Patient_GetPatient = 22
    proc_Patient_SetPatient = 23

    proc_Pay_GetPay = 24
    proc_Pay_SetPay = 25
    proc_Pay_CancelPay = 26
    proc_Pay_UpdatePayByPrice = 27

    proc_PayItem_GetPayItem = 28
    proc_PayItem_SetPayItem = 29

    proc_Reception_CancelReception = 30
    proc_Reception_GetReception = 31
    proc_Reception_GetReceptionBoard = 32
    proc_Reception_SetReception = 33
    proc_Reception_SetReceptionByIRC = 34
    proc_Reception_SetReceptionByRES = 35

    proc_RefreshToken_GetRefreshToken = 36
    proc_RefreshToken_SetRefreshToken = 37

    proc_Reservation_GetReservation = 38
    proc_Reservation_MoveReservationDate = 39
    proc_Reservation_SetReservation = 40
    proc_Reservation_SetReservationByStatus = 41

    proc_Suga_GetSuga = 42
    proc_Suga_SetSuga = 43
    proc_Suga_SetSugaProperty = 44

    proc_Order_GetOrder = 45
    
    proc_NaverPay_SetNaverPay = 46