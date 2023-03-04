from django.urls import path

from api.views import book_list


urlpatterns = [
    path('', book_list)
]
