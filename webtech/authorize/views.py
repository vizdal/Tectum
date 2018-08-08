import os
from .forms import RegisterForm
from django.core import serializers
from django.shortcuts import render,render_to_response,redirect
from authorize.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.validators import validate_email
from .passwordhash import PasswordHasher
from django.contrib.auth import authenticate, login

class Authorize():

    def register(request):
        print('register called')
        print(request.method)
        register_form = RegisterForm
        context = {'form': register_form}
        if request.method == 'POST':
            register_form = register_form(request.POST)
            context = {'form': register_form}
            print('inside post register')
            if register_form.is_valid():
                print('form valid')
                user_email = register_form.cleaned_data['user_email']
                user_password = register_form.cleaned_data['user_password']
                user_cpassword = register_form.cleaned_data['user_cpassword']
                print(user_cpassword)
                user_name = register_form.cleaned_data['user_name']
                print(user_name)
                user_dob = register_form.cleaned_data['user_dob']
                user_country = register_form.cleaned_data['user_country']
                num_results = User.objects.filter(user_email=register_form.cleaned_data['user_email']).count()
                if 0 < num_results:
                    print('User does not exist')
                    # Already an user
                    return
                else:
                    print('for new User')
                    if user_password == user_cpassword:
                        #user = User.objects.get(user_email=user_email)
                        print('same password')
                        hasher = PasswordHasher()
                        user_password = hasher.hash(user_password)
                        user_cpassword = hasher.hash(user_cpassword)
                        #user_country = register_form.cleaned_data['user_country']
                        user, created = User.objects.get_or_create(user_email=user_email, user_password=user_password, user_cpassword=user_cpassword, user_dob=user_dob, user_name=user_name, user_country=user_country)

                        return redirect('/profile/profileedit/')
        else:
            print('signup form called')
            return render(request, 'signup1.html')

    def login(request):
        #login_form = RegisterForm
        #login_form = login_form(request.POST)
        if request.method == 'POST':
            print('inside post')
            user_email = request.POST['user_email']
            print(user_email)
            user_password = request.POST['user_password']
            hasher = PasswordHasher()
            user_password = hasher.hash(user_password)
            count = User.objects.filter(user_email=user_email,user_password=user_password).count()
            if count != 0:
                resultuser = User.objects.filter(user_email=user_email, user_password=user_password)
                print(resultuser)
                print(resultuser[0].user_id)
                return
            else:
                error = 'invalid credentials'
                return render(request, 'login.html',{error:error})
        return render(request, 'login.html')


