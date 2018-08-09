from django.contrib.auth import login, authenticate
from django.shortcuts import render_to_response, render, redirect
from .forms import RegisterForm
from django.template import RequestContext
from django.contrib.auth import logout
from profile.models import Profile
from django.contrib.auth.models import User

def authorize(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            saved_row = form.save()
            profile =  Profile(first_name=form.cleaned_data.get('first_name'),last_name = form.cleaned_data.get('last_name'),email=form.cleaned_data.get('email'),phone=form.cleaned_data.get('phone'),gender= form.cleaned_data.get('gender'),is_veg='N',is_smoke='N',is_alcohol='N',university='Dalhousie',branch='CSE')
            values = profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print(profile.user_id)
            return render_to_response('home.html',{'profile_user_id':profile.user_id},locals())
        else:
            return render(request, 'signup.html', {'form': form})
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
        email = User.objects.get(username=username).email
        profile = Profile.objects.get(email=email)        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:               
                user = authenticate(username=username, password=password)
                login(request, user)
                return render(request, 'home.html',{'profile_user_id':profile.user_id})#render_to_response('home.html',{'profile_user_id':profile.user_id},locals())
    else:
        return render(request,'login.html')