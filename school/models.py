from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model):
    reg_no = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    year_of_study = models.IntegerField(validators=[MinValueValidator(1)])
    image_path = models.URLField(max_length=255, unique=True, null=True)
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
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    year_studied = models.IntegerField()
    sem_studied = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.student} enrolled in {self.course}'
    
    