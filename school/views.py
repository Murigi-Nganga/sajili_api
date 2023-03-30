from django.http import Http404
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     RetrieveAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from api.mixins import PartialUpdateMixin
from school.models import (Admin, Course, Enrollment, Lecturer, Student,
                        Subject)
from django.contrib.auth.hashers import check_password
from school.serializers import (AdminLoginSerializer, AdminSerializer,
                             CourseSerializer, EnrollmentSerializer,
                             LecturerLoginSerializer, LecturerSerializer,
                             StudentLoginSerializer, StudentSerializer, SubjectSerializer)

# Create your views here.
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


class LecturerLogin(APIView):
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            lecturer = Lecturer.objects.get(email=email)
            if lecturer and check_password(password, lecturer.password):
                serializer = LecturerLoginSerializer(lecturer)
                return Response(serializer.data)
            return Response('Wrong email and password combination')
        except Lecturer.DoesNotExist:
            raise Http404


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
    
class EnrollmentList(ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer