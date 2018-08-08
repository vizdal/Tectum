from django.shortcuts import render

# Create your views here.
def index(request):
    #request.META["CSRF_COOKIE_USED"] = True
    return render(request, 'home.html')

# Create your views here.
def welcome(request):
    #request.META["CSRF_COOKIE_USED"] = True
    return render(request, 'welcome.html')
