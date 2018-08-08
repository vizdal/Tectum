from django.shortcuts import render
from .forms import ApartmentForm
from django.http import HttpResponse,HttpResponseRedirect
from Apartments.models import Apartment

# Create your views here.
def index(request,user_id):
	return render(request,'owner.html')

def insert_apartment_details(request,user_id):
	if request.method == 'POST':
		apartment_form = ApartmentForm(request.POST)
		if apartment_form.is_valid():
			apartment_form = apartment_form.save()
			print("sucess")
			if apartment_form.apartment_id:
				return HttpResponseRedirect("/apartments/owner/" + str(user_id),{'is_owner': True})
			else:
				return render(request, 'owner.html', {'apartment_form': apartment_form})
		else:
			print(apartment_form.errors)
			return render(request,'owner.html',{'apartment_form':apartment_form})

def edit_apartment_details(request, apartment_id):
    request.META["CSRF_COOKIE_USED"] = True
    apartment_id = int(apartment_id)
    apartment = Apartment.objects.get(apartment_id=apartment_id)
    return render(request, 'owner.html',{'profile_form':apartment,'saved_row':apartment,'is_update':1})

