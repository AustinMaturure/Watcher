from django.urls import path, include
from .views import getMessage

urlpatterns = [
    path('getmessage/', getMessage)
]
