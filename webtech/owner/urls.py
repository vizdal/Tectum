from django.contrib import admin
from django.urls import include,path
from owner.views import index

urlpatterns = [
    path('<int:user_id>/',index,name="Owner Index"),
]
