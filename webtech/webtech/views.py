from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from profile.forms import ProfileForm
from profile.models import Profile
from django.http import HttpResponse

# Create your views here.
def index(request):
    #request.META["CSRF_COOKIE_USED"] = True
    return render(request, 'home.html')

# Create your views here.
def welcome(request):
    #request.META["CSRF_COOKIE_USED"] = True
    return render(request, 'welcome.html')

@csrf_exempt
def paymentredirect(request):
    email = request.POST['payer_email']
    amount_paid = request.POST['mc_gross']
    profile_object = Profile.objects.get(email=email);
    profile_object.credits = amount_paid
    profile_object.save()
    return HttpResponse()

