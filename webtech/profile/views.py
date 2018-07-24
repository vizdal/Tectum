from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProfileForm
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.`
#To load profile form
def profile_form(request):
    request.META["CSRF_COOKIE_USED"] = True
    return render(request,'profile-edit.html')

def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        #print(form['is_veg'])
        if profile_form.is_valid():
            saved_row = profile_form.save()
            return render(request,'profile.html', { 'saved_row':saved_row })
            #return render(request,'profile.html')
        else:
             return render(request,'profile-edit.html')
    else:
        return HttpResponse('bye')
