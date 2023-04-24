from rest_framework.generics import (ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from api.mixins import PartialUpdateMixin
from api.models import (Attendance, Issue, Location, Schedule)
from api.serializers import (AttendanceSerializer, IssueSerializer,
                             LocationSerializer, ScheduleSerializer,)
from school.models import Subject


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
    
# Get subjects taught by a lecturer
class ScheduleListByLecturer(ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        lecturer_id = self.kwargs['lecturer_id']
        return Schedule.objects.filter(lecturer=lecturer_id)
    
class ScheduleListByStudent(ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        year_of_study = self.kwargs['year_of_study']
        print(year_of_study)
        subjects = Subject.objects.filter(year_studied=year_of_study) 
        print(subjects)
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
