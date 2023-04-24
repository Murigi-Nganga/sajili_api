from django.urls import path, re_path

from api.views import (AttendanceDetail, AttendanceList, IssueDetail, IssueList, 
                       LocationDetail, LocationList, ScheduleDetail, ScheduleList, 
                       ScheduleListByLecturer, ScheduleListByStudent)

urlpatterns = [
    path('issues', IssueList.as_view(), name='issue-list'),
    path('issue/<str:pk>', IssueDetail.as_view(), name='issue-detail'),
    path('schedules', ScheduleList.as_view(), name='schedule-list'),
    path('schedules-by-lec/<int:lecturer_id>', ScheduleListByLecturer.as_view(), name='schedule-list-by-lec'),
    path('schedules-by-student/<int:year_of_study>', ScheduleListByStudent.as_view(), name='schedule-list-by-student'),
    path('schedule/<str:pk>', ScheduleDetail.as_view(), name='schedule-detail'),
    path('attendances', AttendanceList.as_view(), name='admin-list'),
    path('attendance/<str:pk>', AttendanceDetail.as_view(), name='admin-detail'),
    path('locations', LocationList.as_view(), name='location-list'),
    path('location/<str:pk>', LocationDetail.as_view(), name='location-detail'),
]
