from django.urls import path, re_path

from api.views import (AttendanceDetail, AttendanceList, CourseDetail, CourseList, 
                       EnrollmentDetail, EnrollmentList, IssueDetail, IssueList, 
                       LocationDetail, LocationList, ScheduleDetail, ScheduleList, 
                       StudentList, StudentDetail, StudentLogin, LecturerList, 
                       LecturerDetail, LecturerLogin, AdminList, AdminDetail, 
                       AdminLogin, SubjectDetail, SubjectList)

urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
    path('student/<str:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('student/login', StudentLogin.as_view(), name='student-login'),
    path('lecturers/', LecturerList.as_view(), name='lecturer-list'),
    path('lecturer/<str:pk>/', LecturerDetail.as_view(), name='lecturer-detail'),
    path('lecturer/login', LecturerLogin.as_view(), name='lecturer-login'),
    path('admins/', AdminList.as_view(), name='admin-list'),
    path('admin/<str:pk>/', AdminDetail.as_view(), name='admin-detail'),
    path('admin/login', AdminLogin.as_view(), name='admin-login'),
    path('courses/', CourseList.as_view(), name='course-list'),
    path('course/<str:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subject/<str:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('issues/', IssueList.as_view(), name='issue-list'),
    path('issue/<str:pk>/', IssueDetail.as_view(), name='issue-detail'),
    path('schedules/', ScheduleList.as_view(), name='schedule-list'),
    path('schedule/<str:pk>/', ScheduleDetail.as_view(), name='schedule-detail'),
    path('attendances/', AttendanceList.as_view(), name='admin-list'),
    path('attendance/<str:pk>/', AttendanceDetail.as_view(), name='admin-detail'),
    path('locations/', LocationList.as_view(), name='location-list'),
    path('location/<str:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('enrollments/', EnrollmentList.as_view(), name='enrollment-list'),
    path('enrollment/<str:pk>/', EnrollmentDetail.as_view(), name='enrollment-detail'),
    # re_path(r'^.*/$', NotFound.as_view(), name='view-not-found'),
]
