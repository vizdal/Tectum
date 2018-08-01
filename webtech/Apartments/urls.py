from django.contrib import admin
from django.urls import include,path
from Apartments.views import Apartment_list_view

urlpatterns = [
    path('',Apartment_list_view.all_apartments),

]