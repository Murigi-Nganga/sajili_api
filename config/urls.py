"""sajili URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('school/', include('school.urls')),
    path('stats/', include('stats.urls'))
]
