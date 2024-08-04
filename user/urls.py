from django.contrib import admin
from django.urls import path
from .views import UserEndPoint

urlpatterns = [
    path('', UserEndPoint.as_view()),
]