from django.shortcuts import render
# Create your views here.

#To load profile form
def profile_form(request):
    request.META["CSRF_COOKIE_USED"] = True
    return render(request,'profile-edit.html')
