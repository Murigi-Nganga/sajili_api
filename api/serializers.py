from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api.models import (Admin, Attendance, Course, Enrollment, 
                        Issue, Lecturer, Location, Schedule, 
                        Student, Subject)
from api.utils import generate_access_token


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return generate_access_token(obj.pk)


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class StudentSerializer(UserSerializer):

    class Meta:
        fields = '__all__'
        model = Student
        extra_kwargs = {'password': {'write_only': True}}


class StudentLoginSerializer(UserLoginSerializer):
    class Meta:
        fields = '__all__'
        model = Student
        extra_kwargs = {'password': {'write_only': True}}


class LecturerSerializer(UserSerializer):
    class Meta:
        fields = '__all__'
        model = Lecturer
        extra_kwargs = {'password': {'write_only': True}}


class LecturerLoginSerializer(UserLoginSerializer):
    class Meta:
        fields = '__all__'
        model = Lecturer
        extra_kwargs = {'password': {'write_only': True}}


class AdminSerializer(UserSerializer):
    class Meta:
        fields = '__all__'
        model = Admin
        extra_kwargs = {'password': {'write_only': True}}


class AdminLoginSerializer(UserLoginSerializer):
    class Meta:
        fields = '__all__'
        model = Admin
        extra_kwargs = {'password': {'write_only': True}}

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Course
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Subject
        
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
        
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Enrollment
        