from django.contrib import admin
from django.urls import include,path
from profile.views import profile_form

urlpatterns = [
    path('',profile_form,name="profile_form"),
]
