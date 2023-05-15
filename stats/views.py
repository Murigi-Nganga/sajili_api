from django.shortcuts import render

# Create your views here
# TODO: Send email to students who have a poor attendance rate with info that they need to have:
# TODO: Add statistics for:
#? Individual
#*1. Individual biometrics used --> pie chart
#*2. Overall individual attendance percentage - all classes (present, absent)
#*3. Individual attendance percentage by subject (present, absent, remaining to reach 60%)
#* Total number of issues raised + those pardoned
#* Show if red flag or not

#? Lecturers
#* Categories
#* 1. Student --> The individual stats described above
#* 2. Single Subject
#* --> Overall attendance in a line graph
#* --> Biometric method used --> in a pie chart
#* --> Total number of issues raised + those pardoned --> bar plot
#* 3. All subjects
#* --> Overall attendance in a line graph
#* --> Biometric method used --> pie chart
#* --> Total number of issues raised + those pardoned --> bar plot
#* 4. Red Flag students --> Be in cards that will lead to the individual statistics page
#* Add a method to email the student
#* 5. Attendance rate by year

#? General statistics - Web dashboard
#* Categories
#* 1. Overall
#* --> Biometric methods used
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
#* --> Method used to sign attendance
#* --> Attendance by the time of day
#* --> Attendance by day of week
#* --> Total number of issues raised and the number of issues pardoned
#* --> Number of red flag students
#* The list of the red flag students

