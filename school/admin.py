from django.contrib import admin

from school.models import Admin, Course, Enrollment, Lecturer, Student, Subject

# Register your models here.
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Admin)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Enrollment)
