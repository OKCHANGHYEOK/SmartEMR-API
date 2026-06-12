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
    proc_ChartCommonCode_GetChartCommonCode = 11
    proc_Reception_GetReception = 12
    proc_Reception_SetReception = 13
