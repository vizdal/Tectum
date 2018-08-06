import os
from django.core import serializers
from django.shortcuts import render,render_to_response
from Apartments.models import Apartment
from django.http import HttpResponse,HttpResponseRedirect
#from Apartments.filters import ApartmentFilter


class Apartment_list_view():

    def all_apartments(request):
        allApartments = Apartment.objects.all()
        args = {'allApartments' : allApartments,'count':allApartments.count}
        return render(request, "apartment.html", args)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context