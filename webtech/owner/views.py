from django.shortcuts import render
from .forms import ApartmentForm
from django.http import HttpResponse,HttpResponseRedirect
from Apartments.models import Apartment
from profile.models import Profile
import os
import datetime
# Create your views here.
def index(request,user_id):
	return render(request,'owner.html')
#To upload image # This was copy pasted
def handle_uploaded_file(f,filename):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def insert_apartment_details(request,user_id):
	if request.method == 'POST':   
		apartment_form = ApartmentForm(request.POST,request.FILES)
		apartment_id = None
		if apartment_form.is_valid():
			apartment_value = apartment_form.save()
			if len(request.FILES) != 0:
				filename, file_extension = os.path.splitext(request.FILES['apartment_image'].name)
				constructed_file_name = 'apt_'+str(apartment_value.apartment_id)+file_extension
				tot_path = 'pro_image/'+ constructed_file_name
				handle_uploaded_file(request.FILES['apartment_image'],'static/images/'+tot_path)
				apartment_value.apartment_image  = 'images/'+tot_path
				apartment_value.save();
			if apartment_value.apartment_id:
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

