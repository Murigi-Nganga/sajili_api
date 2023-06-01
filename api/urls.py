from django.urls import path, re_path

from api.views import (AttendanceDetail, AttendanceList, CreateAttendance,
                       LocationDetail, LocationList, ScheduleDetail, ScheduleList, 
                       ScheduleListByLecturer, ScheduleListByYear)

urlpatterns = [
    path('schedules', ScheduleList.as_view(), name='schedule-list'),
    path('schedules-by-lec/<int:lecturer_id>', ScheduleListByLecturer.as_view(), name='schedule-list-by-lec'),
    path('schedules-by-year/<int:year_of_study>', ScheduleListByYear.as_view(), name='schedule-list-by-year'),
    path('schedule/<str:pk>', ScheduleDetail.as_view(), name='schedule-detail'),
    path('attendances', AttendanceList.as_view(), name='attendance-list'),
    path('attendance/create', CreateAttendance.as_view(), name='create-attendance'),
    path('attendance/<str:pk>', AttendanceDetail.as_view(), name='attendance-detail'),
    path('locations', LocationList.as_view(), name='location-list'),
    path('location/<str:pk>', LocationDetail.as_view(), name='location-detail'),
]
