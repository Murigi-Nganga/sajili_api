from django.shortcuts import render

# Create your views here
# TODO: Send email to students who have a poor attendance rate with info that they need to have:
# TODO: Add statistics for:
#? Individual
#*2. Overall individual attendance percentage - all classes (present, absent)
#*3. Individual attendance percentage by subject (present, absent, remaining to reach 60%)
#* Show if red flag or not [Has not met 60%]

#? Lecturers
#* Categories
#* 1. Student --> The individual stats described above
#* 2. Single Subject
#* --> Overall attendance in a line graph
#* 3. All subjects
#* --> Overall attendance in a line graph
#* 4. Red Flag students --> Be in cards that will lead to the individual statistics page
#* Add a method to email the student
#* 5. Attendance rate by year

#? General statistics - Web dashboard
#* Categories
#* 1. Overall
#* --> Geographic location information in terms of location attendance percentage
#* --> Lecturer with the most attended classes --> should go to lec's page
#* --> Subject with the most attendance
#* --> Attendance by the time of day
#* --> Attendance by day of week
#* --> Total number of issues raised and the number of issues pardoned 
#* --> Number of red flag students
#* --> Attendance rate by year of study
#* 2. Student
#* Use individual statistics
#* 3. Lecturer
#* Use Lecturer statistics
#* 4. Subject
#* --> Attendance by the time of day
#* --> Attendance by day of week
#* --> Total number of issues raised and the number of issues pardoned
#* --> Number of red flag students
#* The list of the red flag students


#? Function to calculate the number of occurrences of a schedule
#? Shows the number of present classes, complement will be absent classes
#? Return the same in % form
#* from datetime import datetime, timedelta

#* def count_schedule_occurrences(start_date, end_date, schedule_days):
#*     count = 0
#*     current_date = start_date

#*     while current_date <= end_date:
#*         if current_date.strftime('%A') in schedule_days:
#*             count += 1
#*         current_date += timedelta(days=1)

#*     return count

#* # Example usage
#* start_date = datetime(2023, 1, 1)
#* end_date = datetime(2023, 12, 31)
#* schedule_days = ['Tuesday', 'Wednesday', 'Friday']

#* schedule_count = count_schedule_occurrences(start_date, end_date, schedule_days)
#* print("Number of schedule occurrences:", schedule_count)
