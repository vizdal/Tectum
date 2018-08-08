from django.contrib import admin
from django.urls import include, path
from owner.views import index, insert_apartment_details, edit_apartment_details

urlpatterns = [
    path('<int:user_id>/',index,name="Owner Index"),
    path('<int:user_id>/save/',insert_apartment_details,name="Save Apartment"),
    path('apartment/<int:apartment_id>',edit_apartment_details,name="Save Apartment")

]
