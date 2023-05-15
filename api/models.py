from django.db import models

from school.models import Lecturer, Student, Subject

class Location(models.Model):
    name = models.CharField(max_length=255)
    
    #* storing polygon points as a string - which is a list of lists
    polygon_points = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.name

class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE) 
    day_of_week = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_online = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.subject} in {self.location}'
    
class Issue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.student}: {self.message}'
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    method_used = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.student}: {self.schedule}'
    