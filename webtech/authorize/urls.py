from django.contrib import admin
from django.urls import include,path
from authorize.views import Authorize

urlpatterns = [
    path('register/',Authorize.register),
    path('login/',Authorize.login),
]