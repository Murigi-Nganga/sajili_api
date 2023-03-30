from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api.models import (Attendance, Issue, Location, Schedule)

        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Attendance
        
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Issue
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Location
        
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Schedule
        
        