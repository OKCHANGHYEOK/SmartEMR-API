from enum import Enum

class eSP(Enum):
    proc_Member_GetMember = 0
    proc_Member_SetMember = 1
    proc_MemberUser_GetMemberUser = 2
    proc_MemberUser_SetMemberUser = 3
    proc_Patient_GetPatient = 4
    proc_Patient_SetPatient = 5
    proc_Chart_GetChart = 6
    proc_Chart_SetChart = 7
    proc_ChartCommonCode_GetChartCommonCode = 8