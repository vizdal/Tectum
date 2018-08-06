from django.shortcuts import render
from .forms import FeedbackForm
import sys
sys.path.append("..")
from Apartments.models import Apartment

# Create your views here.
def feedback_form(request,user_id):
    request.META["CSRF_COOKIE_USED"] = True
    current_user_id = int(user_id)
    allApartments = Apartment.objects.all()
    return render(request,'feedback.html',{'user_id':user_id, 'allApartments':allApartments})

def save_feedback(request):
    if request.method == 'POST':
        is_success = False
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save();
            is_success = True
            print("aman")
            return render(request,'feedback_thanks.html')
        print(feedback_form.errors)
        allApartments = Apartment.objects.all()
        return render(request,'feedback.html',{'feedback_form':feedback_form, 'allApartments':allApartments})

def get_apartment_names(request):
    allApartments = Apartment.objects.all()
   #print('check')
    args = {'allApartments': allApartments}
    return render(request, "feedback.html", args)
