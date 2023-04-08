from django.contrib import admin

from api.models import Attendance, Issue, Location, Schedule

# Register your models here
admin.site.register(Issue)
admin.site.register(Schedule)
admin.site.register(Attendance)
admin.site.register(Location)