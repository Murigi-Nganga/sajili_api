from django.contrib import admin

from api.models import Attendance, Location, Schedule

# Register your models here
admin.site.register(Schedule)
admin.site.register(Attendance)
admin.site.register(Location)