from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api.models import (Attendance, Issue, Location, Schedule)
from school.serializers import LecturerSerializer, StudentSerializer
        
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Issue
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Location
        
class ScheduleSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer()
    class Meta:
        fields = '__all__'
        model = Schedule
        depth = 1
        
class CUDAttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Attendance
        
class RetrieveAttendancesSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer()
    student = StudentSerializer()
    
    class Meta:
        fields = '__all__'
        model = Attendance
        depth = 2
        
    
        