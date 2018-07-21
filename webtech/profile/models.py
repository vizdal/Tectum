from django.db import models
import json

# Create your models here.

class Profile(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('N', 'Prefer Not to Mention'),
    )
    gender = models.CharField(max_length=1, choices=gender_options)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    university = models.CharField(max_length=100)
    branch = models.CharField(max_length=70)
    is_veg = models.BooleanField(default=True)
    is_smoke = models.BooleanField(default=False)
    is_alcohol = models.BooleanField(default=False)
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
