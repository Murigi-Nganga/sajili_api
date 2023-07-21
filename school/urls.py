
from django.urls import path

from school.views import AdminDetail, AdminList, AdminLogin, CourseList, EnrollmentDetail, EnrollmentList, \
    LecturerDetail, LecturerList, LecturerLogin, StudentDetail, StudentList, StudentLogin, StudentUpdateWithPhoto, \
    SubjectDetail, SubjectList, SubjectListByLecturer, CourseDetail

urlpatterns = [
    path('students', StudentList.as_view(), name='student-list'),
    path('student/login', StudentLogin.as_view(), name='student-login'),
    path('student/<str:pk>', StudentDetail.as_view(), name='student-detail'),
    path('student/submit-photo', StudentUpdateWithPhoto.as_view(), name='student-upload-photo'),
    path('lecturers', LecturerList.as_view(), name='lecturer-list'),
    path('lecturer/login', LecturerLogin.as_view(), name='lecturer-login'),
    path('lecturer/<str:pk>', LecturerDetail.as_view(), name='lecturer-detail'),
    path('admins', AdminList.as_view(), name='admin-list'),
    path('admin/login', AdminLogin.as_view(), name='admin-login'),
    path('admin/<str:pk>', AdminDetail.as_view(), name='admin-detail'),
    path('courses', CourseList.as_view(), name='course-list'),
    path('course/<str:pk>', CourseDetail.as_view(), name='course-detail'),
    path('subjects', SubjectList.as_view(), name='subject-list'),
    path('subjects-by-lec/<int:lecturer_id>', SubjectListByLecturer.as_view(), name='subject-list-by-lec'),
    path('subject/<str:pk>', SubjectDetail.as_view(), name='subject-detail'),
    path('enrollments', EnrollmentList.as_view(), name='enrollment-list'),
    path('enrollment/<str:pk>', EnrollmentDetail.as_view(), name='enrollment-detail'),
]
