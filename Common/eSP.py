from enum import Enum

class eSP(Enum):
    proc_CommonCode_GetCommonCode = 0

    proc_Consultation_GetConsultation = 1
    proc_Consultation_GetConsultationByRCP = 2
    proc_Consultation_SetConsultation = 3

    proc_Insurance_GetInsurance = 4
    proc_Insurance_SetInsurance = 5

    proc_Member_GetMember = 6
    proc_Member_SetMember = 7

    proc_MemberUser_GetMemberUser = 8
    proc_MemberUser_GetMemberUserForLogin = 9
    proc_MemberUser_SetMemberUser = 10

    proc_Patient_GetPatient = 11
    proc_Patient_SetPatient = 12

    proc_Pay_GetPay = 13
    proc_Pay_SetPay = 14

    proc_Reception_CancelReception = 15
    proc_Reception_GetReception = 16
    proc_Reception_GetReceptionBoard = 17
    proc_Reception_SetReception = 18
    proc_Reception_SetReceptionByIRC = 19
    proc_Reception_SetReceptionByRES = 20

    proc_RefreshToken_GetRefreshToken = 21
    proc_RefreshToken_SetRefreshToken = 22

    proc_Reservation_GetReservation = 23
    proc_Reservation_MoveReservationDate = 24
    proc_Reservation_SetReservation = 25
    proc_Reservation_SetReservationByStatus = 26