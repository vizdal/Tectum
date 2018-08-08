from django.shortcuts import render
from .forms import ApartmentForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request,user_id):
	return render(request,'owner.html')

def insert_apartment_details(request,user_id):
	if request.method == 'POST':
		apartment_form = ApartmentForm(request.POST,request.FILES)
		if apartment_form.is_valid():
			apartment_form.save()
			return render(request,'owner.html',{'is_saved':True})
		else:
			return render(request,'owner.html',{'apartment_form':apartment_form})

