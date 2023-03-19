from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model):
    reg_no = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255)
    year_of_study = models.IntegerField(validators=[MinValueValidator(1)])
    image_path = models.URLField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.reg_no

class Lecturer(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Admin(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=15)
    
    def __str__(self):
        return self.email
    
class Location(models.Model):
    name = models.CharField(max_length=255)
    center_lat = models.DecimalField(max_digits=4, decimal_places=2)
    center_long = models.DecimalField(max_digits=4, decimal_places=2)
    radius = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Issue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.student}: {self.message}'
    
class Subject(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    year_studied = models.IntegerField()
    sem_studied = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_online = models.BooleanField()
    
    def __str__(self):
        return f'{self.subject} in {self.location}'
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.student}: {self.schedule}'
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.student} enrolled in {self.course}'
    