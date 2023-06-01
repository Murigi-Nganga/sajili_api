from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     ListAPIView)
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
from school.utils import get_facial_encodings

wrong_credentials_response = Response({'message': 'Wrong email and password combination'},
                                      status=status.HTTP_404_NOT_FOUND)

class StudentLogin(APIView):
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            student = Student.objects.get(email=email)
            if check_password(password, student.password):
                serializer = StudentLoginSerializer(student)
                return Response(serializer.data)
            return wrong_credentials_response
        except Student.DoesNotExist:
            return wrong_credentials_response


class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentUpdateWithPhoto(APIView):
    allowed_methods = ['POST']
    
    def post(self, request):
        reg_no = request.data.get('reg_no')

        try:
            student = Student.objects.get(pk=reg_no)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)

        image = request.FILES.get('student_image')

        face_encodings = get_facial_encodings(image)
        student.face_encodings = face_encodings
        student.save()
        
        return Response({'message': 'Image processed successfully'}, status=200)


class LecturerLogin(APIView):
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            lecturer = Lecturer.objects.get(email=email)
            if check_password(password, lecturer.password):
                serializer = LecturerLoginSerializer(lecturer)
                return Response(serializer.data)
            return wrong_credentials_response
        except Lecturer.DoesNotExist:
            return wrong_credentials_response


class LecturerList(ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LecturerDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class AdminLogin(APIView):
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            admin = Admin.objects.get(email=email)
            if check_password(password, admin.password):
                serializer = AdminLoginSerializer(admin)
                return Response(serializer.data)
            return wrong_credentials_response
        except Admin.DoesNotExist:
            return wrong_credentials_response


class AdminList(ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


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

# Get subjects taught by a lecturer
class SubjectListByLecturer(ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        lecturer_id = self.kwargs['lecturer_id']
        return Subject.objects.filter(lecturer=lecturer_id)


class SubjectDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class EnrollmentList(ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
