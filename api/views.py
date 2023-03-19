from django.http import Http404
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     RetrieveAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.status import HTTP_404_NOT_FOUND
from api.mixins import PartialUpdateMixin
from api.models import (Admin, Attendance, Course, Enrollment,
                        Issue, Lecturer, Location, Student,
                        Subject, Schedule)
from django.contrib.auth.hashers import check_password
from api.serializers import (AdminLoginSerializer, AdminSerializer, AttendanceSerializer,
                             CourseSerializer, EnrollmentSerializer, IssueSerializer,
                             LecturerLoginSerializer, LecturerSerializer,
                             LocationSerializer, ScheduleSerializer,
                             StudentLoginSerializer, StudentSerializer, SubjectSerializer)


class StudentLogin(APIView):
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            student = Student.objects.get(email=email)
            if student and check_password(password, student.password):
                serializer = StudentLoginSerializer(student)
                return Response(serializer.data)
            return Response('Wrong email and password combination')
        except Student.DoesNotExist:
            raise Http404


class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class LecturerLogin(RetrieveAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerLoginSerializer


class LecturerList(ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LecturerDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class AdminLogin(RetrieveAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminLoginSerializer


class AdminList(ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = LecturerSerializer


class AdminDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class CourseList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SubjectList(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class AttendanceList(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class LocationList(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ScheduleList(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class IssueList(ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class EnrollmentList(ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# class NotFound(APIView):
#     def get(self, request, format=None):
#         return Response({"detail": "Not found."}, status=HTTP_404_NOT_FOUND)