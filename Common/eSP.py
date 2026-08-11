from enum import Enum

class eSP(Enum):
    proc_CommonCode_GetCommonCode = 0

    proc_Consultation_GetConsultation = 1
    proc_Consultation_SetConsultation = 2

    proc_Insurance_GetInsurance = 3
    proc_Insurance_SetInsurance = 4

    proc_Member_GetMember = 5
    proc_Member_SetMember = 6

    proc_MemberUser_GetMemberUser = 7
    proc_MemberUser_GetMemberUserForLogin = 8
    proc_MemberUser_SetMemberUser = 9

    proc_Patient_GetPatient = 10
    proc_Patient_SetPatient = 11

    proc_Pay_GetPay = 12
    proc_Pay_SetPay = 13

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