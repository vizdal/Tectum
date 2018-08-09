import os
from django.core import serializers
from django.shortcuts import render,render_to_response
from Apartments.models import Apartment
import sys
sys.path.append("..")
from feedback.models import Feedback

from django.http import HttpResponse,HttpResponseRedirect
#from Apartments.filters import ApartmentFilter


class Apartment_list_view():
    def all_apartments(request):
        allApartments = Apartment.objects.all()
        args = {'allApartments' : allApartments,'count':allApartments.count}
        return render(request, "apartment.html", args)
    def apartment_form(request, apartment_id):
        request.META["CSRF_COOKIE_USED"] = True
        apartment_id = int(apartment_id)
        apartment = Apartment.objects.get(apartment_id=apartment_id)
        units=apartment.available_units
        print("Available Units are"+units)
        data = units.split(",")
        print(data[0])
        feedback = None
        try:
            feedback=Feedback.objects.get(apartment_id=apartment_id)
        except:
            print('No Feedback')
        return render(request, 'apartment_list.html', {'apartment': apartment, 'feedback': feedback,'data':data})

    def apartment_by_user(request, user_id):
        request.META["CSRF_COOKIE_USED"] = True
        user_id = int(user_id)
        apartments = Apartment.objects.filter(user_id=user_id)
        args = {'allApartments': apartments, 'count': apartments.count, 'is_owner':True}
        return render(request, "apartment.html", args)

    def all_apartment(request):
        allApartments = Apartment.objects.all()
        args = {'allApartments' : allApartments }
        return render(request, "feedback.html", args)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context