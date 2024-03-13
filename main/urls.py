from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main1, name="main"),
    path("/tutors", views.tutors, name="tutors"),
    path("/index", views.index, name="index")
]
