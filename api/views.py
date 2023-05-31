from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView)
from api.mixins import PartialUpdateMixin
from api.models import (Attendance, Issue, Location, Schedule)
from api.serializers import (IssueSerializer, CUDAttendanceSerializer,
                             LocationSerializer, RetrieveAttendancesSerializer, ScheduleSerializer,)
from api.utils import compare_facial_encodings
from api.models import Schedule
from school.models import Student, Subject


class AttendanceList(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = RetrieveAttendancesSerializer


class CreateAttendance(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = CUDAttendanceSerializer

    def post(self, request, *args, **kwargs):
        student_id = request.data.get('student')
        student = Student.objects.get(pk=student_id)
        student_image_file = request.FILES.get('student_image')

        if student_image_file:
            if student.face_image_encodings == None:
                return Response({'message': 'Student image not found. Please visit the admin office.'},
                                status=status.HTTP_404_NOT_FOUND)
            result = compare_facial_encodings(
                student_image_file, student.face_image_encodings)

            if result:
                return self.create(request, *args, **kwargs)

            return Response({'message': 'Authentication failed'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        return self.create(request, *args, **kwargs)


class AttendanceDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = CUDAttendanceSerializer


class LocationList(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ScheduleList(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# Get subject schedules for a lecturer


class ScheduleListByLecturer(ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        lecturer_id = self.kwargs['lecturer_id']
        return Schedule.objects.filter(lecturer=lecturer_id)

# Get schedules by the year of study


class ScheduleListByYear(ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        year_of_study = self.kwargs['year_of_study']
        subjects = Subject.objects.filter(year_studied=year_of_study)
        return Schedule.objects.filter(subject__in=subjects)


class ScheduleDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class IssueList(ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueDetail(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
