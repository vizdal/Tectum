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
        args = {'allApartments' : allApartments }
        return render(request, "apartment.html", args)

    def apartment_form(request, apartment_id):
        request.META["CSRF_COOKIE_USED"] = True
        apartment_id = int(apartment_id)
        feedback=Feedback.objects.get(apartment_id=apartment_id)
        apartment = Apartment.objects.get(apartment_id=apartment_id)
        return render(request, 'apartment_list.html', {'apartment': apartment,'feedback':feedback})

    def all_apartment(request):
        allApartments = Apartment.objects.all()
        args = {'allApartments' : allApartments }
        return render(request, "feedback.html", args)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context