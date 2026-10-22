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
    proc_ConsultationOrder_GetConsultationOrderByRecent = 8
    proc_ConsultationOrder_SetConsultationOrder = 9
    proc_ConsultationOrder_SetConsultationOrderProperty = 10

    proc_EmailVerification_GetEmailVerification = 11
    proc_EmailVerification_GetEmailVerificationByVerify = 12
    proc_EmailVerification_SetEmailVerification = 13

    proc_Insurance_GetInsurance = 14
    proc_Insurance_GetRecentInsurance = 15
    proc_Insurance_SetInsurance = 16

    proc_Member_GetMember = 17
    proc_Member_SetMember = 18
    proc_Member_SetAdminUser = 19

    proc_MemberUser_GetMemberUser = 20
    proc_MemberUser_GetMemberUserForLogin = 21
    proc_MemberUser_SetMemberUser = 22
    proc_MemberUser_ChangePassword = 23

    proc_Patient_GetPatient = 24
    proc_Patient_SetPatient = 25

    proc_Pay_GetPay = 26
    proc_Pay_SetPay = 27
    proc_Pay_CancelPay = 28
    proc_Pay_UpdatePayByPrice = 29

    proc_PayItem_GetPayItem = 30
    proc_PayItem_SetPayItem = 31

    proc_Reception_CancelReception = 32
    proc_Reception_GetReception = 33
    proc_Reception_GetReceptionBoard = 34
    proc_Reception_SetReception = 35
    proc_Reception_SetReceptionByIRC = 36
    proc_Reception_SetReceptionByRES = 37

    proc_RefreshToken_GetRefreshToken = 38
    proc_RefreshToken_SetRefreshToken = 39

    proc_Reservation_GetReservation = 40
    proc_Reservation_MoveReservationDate = 41
    proc_Reservation_SetReservation = 42
    proc_Reservation_SetReservationByStatus = 43

    proc_Suga_GetSuga = 44
    proc_Suga_GetSugaCategory = 45
    proc_Suga_SetSuga = 46
    proc_Suga_SetSugaProperty = 47

    proc_Order_GetOrder = 48
    
    proc_NaverPay_SetNaverPay = 49