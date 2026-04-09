from enum import Enum

class eSP(Enum):
    proc_Member_GetMember = 0
    proc_Member_SetMember = 1
    proc_MemberUser_GetMemberUser = 2
    proc_MemberUser_GetMemberUserForLogin = 3
    proc_MemberUser_SetMemberUser = 4
    proc_Patient_GetPatient = 5
    proc_Patient_SetPatient = 6
    proc_Chart_GetChart = 7
    proc_Chart_SetChart = 8
    proc_ChartCommonCode_GetChartCommonCode = 9