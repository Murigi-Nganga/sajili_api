
from django.urls import path

from school.views import AdminDetail, AdminList, AdminLogin, CourseDetail, CourseList, EnrollmentDetail, EnrollmentList, LecturerDetail, LecturerList, LecturerLogin, StudentDetail, StudentList, StudentLogin, SubjectDetail, SubjectList


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
    path('enrollments/', EnrollmentList.as_view(), name='enrollment-list'),
    path('enrollment/<str:pk>/', EnrollmentDetail.as_view(), name='enrollment-detail'),
]
