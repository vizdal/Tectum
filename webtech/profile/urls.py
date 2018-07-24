from django.contrib import admin
from django.urls import include,path
from profile.views import profile_form,update_profile

urlpatterns = [
    path('',profile_form,name="profile_form"),
    path('update_profile/',update_profile,name="Update Profile")
]
