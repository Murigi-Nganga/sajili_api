from django.db import models

from school.models import Lecturer, Student, Subject

class Location(models.Model):
    name = models.CharField(max_length=255)
    
    #* storing polygon points as a string - which contains a list of lists
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
    
class Attendance(models.Model):
    
    AUTH_METHOD_CHOICES = (
        ("local_auth", "local_auth"),
        ("face_recognition_service", "face_recognition_service"),
        ("other", "other"),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    is_partial = models.BooleanField(default=False)
    auth_method = models.CharField(max_length=30, choices=AUTH_METHOD_CHOICES, default='other')
    time_signed_in = models.DateTimeField()
    
    def __str__(self):
        return f'{self.student}: {self.schedule}'
    