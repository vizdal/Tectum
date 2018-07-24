from django.db import models
from django.core.validators import RegexValidator
import json

# Create your models here.

class Profile(models.Model):
    alphanumeric_validator = RegexValidator(r'^[A-Za-z0-9]*$','Shall Contain only alphabets and numbers')
    alphabet_validator = RegexValidator(r'^[A-Za-z0-9]$','Shall contain only alphabets')
    
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50,validators=[alphanumeric_validator])
    meal_options = (
        ('V','Vegetarian'),
        ('N','Non-Vegetarian')
    )
    last_name = models.CharField(max_length=50)
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('N', 'Prefer Not to Mention')
    )
    smoke_options = (
        ('S','Smoker'),
        ('N','Non-Smoker')
    )

    alcohol_options = (
        ('A','Alcoholic'),
        ('N','Non-Alcoholic')
    )
    gender = models.CharField(max_length=1, choices=gender_options)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    university = models.CharField(max_length=100,validators=[alphanumeric_validator])
    branch = models.CharField(max_length=70,validators=[alphanumeric_validator])
    is_veg = models.CharField(max_length=1, choices=meal_options)
    is_smoke = models.CharField(max_length=1, choices=smoke_options)
    is_alcohol = models.CharField(max_length=1, choices=alcohol_options)
    image_url = models.CharField(max_length=150)

    def __str__():
        return_dict = {}
        return_dict['id'] = user_id
        return_dict['fname'] = first_name
        return_dict['lname'] = last_name
        return_dict['gender'] = gender
        return_dict['email'] = email
        return_dict['phone'] = phone
        return_dict['university'] = university
        return_dict['branch'] = branch
        return_dict['is_veg'] = is_veg
        return_dict['is_smoke'] = is_smoke
        return_dict['is_alcohol'] = is_alcohol
        return_dict['image_url'] = image_url
        return json.dumps(return_dict)
    def get_profile_details(user_id_param):
        return Profile.objects.filter(user_id=user_id_param)
