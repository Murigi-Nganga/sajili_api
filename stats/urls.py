from django.urls import path

from stats.views import WebStatisticsAPIView

urlpatterns = [
    path('web-stats', WebStatisticsAPIView.as_view(), name='att-by-location'),
]
