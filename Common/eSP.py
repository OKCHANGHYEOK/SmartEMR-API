from enum import Enum

class eSP(Enum):
    proc_RefreshToken_GetRefreshToken = 0
    proc_RefreshToken_SetRefreshToken = 1
    proc_Member_GetMember = 2
    proc_Member_SetMember = 3
    proc_MemberUser_GetMemberUser = 4
    proc_MemberUser_GetMemberUserForLogin = 5
    proc_MemberUser_SetMemberUser = 6
    proc_Patient_GetPatient = 7
    proc_Patient_SetPatient = 8
    proc_Chart_GetChart = 9
    proc_Chart_SetChart = 10
    proc_CommonCode_GetCommonCode = 11
    proc_Reservation_GetReservation = 12
    proc_Reservation_SetReservation = 13
    proc_Reservation_SetReservationByStatus = 14
    proc_Reservation_MoveReservationDate = 15
    proc_Reception_GetReception = 16
    proc_Reception_GetReceptionBoard = 17
    proc_Reception_SetReception = 18
    proc_Reception_CancelReception = 19
    proc_Reception_SetReceptionByRES = 20
    proc_Reception_SetReceptionByIRC = 21
    proc_Insurance_GetInsurance = 22
    proc_Insurance_SetInsurance = 23
    proc_Pay_GetPay = 24
    proc_Pay_SetPay = 25
