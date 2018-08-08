from django.contrib import admin
from django.urls import include,path
from Apartments.views import Apartment_list_view

urlpatterns = [
    path('',Apartment_list_view.all_apartments),
    path('<int:apartment_id>/', Apartment_list_view.apartment_form, name="apartment_page"),
    path('owner/<int:user_id>/', Apartment_list_view.apartment_by_user, name="apartment_page"),

]