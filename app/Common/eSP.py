from enum import Enum

class eSP(Enum):
    proc_CommonCode_GetCommonCode = 0

    proc_Consultation_GetConsultation = 1
    proc_Consultation_GetConsultationByRCP = 2
    proc_Consultation_SetConsultation = 3

    proc_Insurance_GetInsurance = 4
    proc_Insurance_GetRecentInsurance = 5
    proc_Insurance_SetInsurance = 6

    proc_Member_GetMember = 7
    proc_Member_SetMember = 8

    proc_MemberUser_GetMemberUser = 9
    proc_MemberUser_GetMemberUserForLogin = 10
    proc_MemberUser_SetMemberUser = 11

    proc_Patient_GetPatient = 12
    proc_Patient_SetPatient = 13

    proc_Pay_GetPay = 14
    proc_Pay_SetPay = 15

    proc_Reception_CancelReception = 16
    proc_Reception_GetReception = 17
    proc_Reception_GetReceptionBoard = 18
    proc_Reception_SetReception = 19
    proc_Reception_SetReceptionByIRC = 20
    proc_Reception_SetReceptionByRES = 21

    proc_RefreshToken_GetRefreshToken = 22
    proc_RefreshToken_SetRefreshToken = 23

    proc_Reservation_GetReservation = 24
    proc_Reservation_MoveReservationDate = 25
    proc_Reservation_SetReservation = 26
    proc_Reservation_SetReservationByStatus = 27

    proc_Suga_GetSuga = 28
    proc_Suga_SetSuga = 29
    proc_Suga_SetSugaProperty = 30