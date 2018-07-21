from django.db import models

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
