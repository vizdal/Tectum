from django.contrib import admin
from django.urls import include,path
from authorize.views import authorize,redirect,logout_user,auth_login

urlpatterns = [
    path('signup/',authorize),	
	path('logout/',logout_user),
    path('',redirect),
    path('login/',auth_login),
]