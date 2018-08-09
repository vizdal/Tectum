from django.contrib.auth import login, authenticate
from django.shortcuts import render_to_response, render, redirect
from .forms import RegisterForm
from django.template import RequestContext
from django.contrib.auth import logout

def authorize(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #hasher = PasswordHasher()
            #user_password = hasher.hash(user_password)            
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render_to_response('home.html', locals())
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

def redirect(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return render_to_response('login.html', locals())
def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['user_password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                user = authenticate(username=username, password=password)
                login(request, user)
                return render_to_response('home.html', locals())
    else:
        return render(request,'login.html')