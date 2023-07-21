from django.shortcuts import render

# Create your views here
# TODO: Send email to students who have a poor attendance rate with info that they need to have:
# TODO: Add statistics for:
# ? Individual
# *2. Overall individual attendance percentage - all classes (present, absent) --> Done
# *3. Individual attendance percentage by subject (present, absent, remaining to reach 60%) --> Done
# * Show if red flag or not [Has not met 60%] --> Done

# ? Lecturers
# * Categories
# * 1. Student --> The individual stats described above
# * 2. Single Subject
# * --> Overall attendance in a line graph
# * 3. All subjects
# * --> Overall attendance in a line graph
# * 4. Red Flag students --> Be in cards that will lead to the individual statistics page
# * Add a method to email the student
# * 5. Attendance rate by year

# ? General statistics - Web dashboard
# * Categories
# * 1. Overall
# * --> Geographic location information in terms of location attendance percentage --> Done
# * --> Lecturer with the most attended classes --> should go to lec's page --> Done
# * --> Subject with the most attendance --> Done
# * --> Attendance by the time of day --> Done
# * --> Attendance by day of week --> Done
# * --> Number of red flag students --> Done
# * --> Attendance rate by year of study --> Done
# * 2. Student
# * Use individual statistics
# * 3. Lecturer
# * Use Lecturer statistics
# * 4. Subject
# * --> Attendance by the time of day
# * --> Attendance by day of week
# * --> Number of red flag students
# * The list of the red flag students

# ? Function to calculate the number of occurrences of a schedule
# ? Shows the number of present classes, complement will be absent classes
# ? Return the same in % form
# * from datetime import datetime, timedelta

# * def count_schedule_occurrences(start_date, end_date, schedule_days):
# *     count = 0
# *     current_date = start_date

# *     while current_date <= end_date:
# *         if current_date.strftime('%A') in schedule_days:
# *             count += 1
# *         current_date += timedelta(days=1)

# *     return count

# * # Example usage
# * start_date = datetime(2023, 1, 1)
# * end_date = datetime(2023, 12, 31)
# * schedule_days = ['Tuesday', 'Wednesday', 'Friday']

# * schedule_count = count_schedule_occurrences(start_date, end_date, schedule_days)
# * print("Number of schedule occurrences:", schedule_count)

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

from api.models import Attendance, Schedule
from school.models import Lecturer, Student, Subject


class StudentAttendanceView(APIView):
    def post(self, request):
        reg_no = request.data.get('reg_no')

        try:
            student_attendances = Attendance.objects.filter(
                student__reg_no=reg_no)
            total_attendance = student_attendances.count()

            return Response({'total_attendance': total_attendance})
        except Attendance.DoesNotExist:
            return Response({'error': 'Student attendance not found'})


class WebStatisticsAPIView(APIView):
    def get(self, request):
        years = {}

        for year in range(1, 5):
            years[year] = Attendance.objects.filter(
                student__year_of_study=year).count()

        subjects = {}
        subject_names = [subject.name for subject in Subject.objects.all()]

        for subject_name in subject_names:
            subjects[subject_name] = Attendance.objects.filter(
                schedule__subject__name=subject_name).count()

        students = {}
        student_names = [[student.first_name, student.second_name]
                         for student in Student.objects.all()]

        for student_name in student_names:
            students[student_name[0] + " " + student_name[1]
                     ] = Attendance.objects.filter(student__first_name=student_name[0]).count()

        lecturers = {}
        lecturer_names = [[lecturer.first_name, lecturer.second_name]
                          for lecturer in Lecturer.objects.all()]

        for lecturer_name in lecturer_names:
            lecturers[lecturer_name[0] + " " + lecturer_name[1]] = Attendance.objects.filter(
                schedule__lecturer__first_name=lecturer_name[0]).count()

        authentications = {}
        auth_methods = ['local_auth', 'face_recognition_service', 'other']

        for auth_method in auth_methods:
            authentications[auth_method] = Attendance.objects.filter(
                auth_method=auth_method).count()

        weekdays = {}
        weekday_names = ['Monday', 'Tuesday',
                         'Wednesday', 'Thursday', 'Friday']

        for weekday_name in weekday_names:
            weekdays[weekday_name] = Attendance.objects.filter(
                schedule__day_of_week=weekday_name).count()

        locations = {}
        location_names = ['LG01', 'Undergraduate Lab',
                          'Masters Lab', 'Millenium Hall']

        for location_name in location_names:
            locations[location_name] = Attendance.objects.filter(
                schedule__location__name=location_name).count()

        return Response({"locations": locations, "years": years, "subjects": subjects,
                         "students": students, "lecturers": lecturers,
                         "authentications": authentications, "weekdays": weekdays,
                         })
