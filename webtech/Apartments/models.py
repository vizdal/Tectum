from django.db import models
from django.core.validators import RegexValidator,EmailValidator
import json
from datetime import date

# Create your models here.
class Apartment(models.Model):

    alphanumeric_validator = RegexValidator(r'^[A-Za-z0-9]*$','Shall Contain only alphabets and numbers')
    alphabet_validator = RegexValidator(r'^[A-Za-z]*$','Shall contain only alphabets')
    numeric_validator = RegexValidator(r'^[0-9]*$','Shall contain only numerals')
    csv_validator = RegexValidator(r'^[0-9,]*$','Should have numbers seperated by commas')
    email_validator = EmailValidator(message='Please check the email address')
    alphabet_and_space_validator = RegexValidator(r'^[A-Za-z\s]*$','Shall contain only alphabets')
    
    available_options = (
        ('Y', 'available'),
        ('N', 'Non-not-available')
    )
    near_by = (
        ('DAL', 'Dalhousie university'),
        ('SMU', 'SMU university'),
        ('WALMART', 'Walmart-Mumfford'),
        ('COSTCO', 'Costco')
    )
    type_of_room = (
        ('1', '1BHK'),
        ('2', '2BHK'),
        ('3', '3BHK'),
        ('B', 'Bungalow'),
        ('S', 'Single Room'),
    )
    sharing = (
        ('Y','Sharing'),
        ('N', 'No-Sharing')
    )
    meal_options = (
        ('V','Vegetarian'),
        ('N','Non-Vegetarian')
    )
    smoke_options = (
        ('S','Smoker'),
        ('N','Non-Smoker')
    )
    alcohol_options = (
        ('A','Alcoholic'),
        ('N','Non-Alcoholic')
    )
    car_parking = (
        ('Y', 'Yes'),
        ('N', 'No-Car-Parking')
    )
    gym = (
        ('Y', 'Yes'),
        ('N', 'No-Gym')
    )
    heater = (
        ('Y', 'Yes'),
        ('N', 'No-heater')
    )

    apartment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('profile.Profile',on_delete=models.CASCADE)
    apartment_name = models.CharField(max_length=50,validators=[alphabet_and_space_validator])
    available_units = models.CharField(max_length=400,default=0,validators=[csv_validator])
    apartment_location = models.CharField(max_length=400,validators=[alphanumeric_validator])
    apartment_description = models.CharField(max_length=400, validators=[alphabet_and_space_validator])
    apartment_price = models.IntegerField(default=0, validators=[numeric_validator])
    near_by = models.CharField(max_length=10, choices=near_by, default='DAL')
    type_of_room = models.CharField(max_length=10, choices=type_of_room,default='2')
    posession = models.DateField(default=date.today)
    is_veg = models.CharField(max_length=1, choices=meal_options,default='N')
    is_smoke = models.CharField(max_length=1, choices=smoke_options,default='N')
    is_alcohol = models.CharField(max_length=1, choices=alcohol_options,default='N')
    sharing_count = models.IntegerField(default=1, validators=[numeric_validator])
    sharing = models.CharField(max_length=1, choices=sharing, default='N')
    car_parking = models.CharField(max_length=1, choices=car_parking, default='N')
    gym = models.CharField(max_length=1, choices=gym, default='N')
    heater = models.CharField(max_length=1, choices=heater, default='N')
    apartment_image = models.ImageField(upload_to='images/', default='images/svg/apartment.svg')

    def clean_posession(self):
        date = self.cleaned_data['posession']
        if date < datetime.date.today():
            raise forms.ValidationError("Date Cannot be in the past!")
        return date

class owner(models.Model):
    alphanumeric_validator = RegexValidator(r'^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')
    alphabet_validator = RegexValidator(r'^[A-Za-z0-9]$', 'Shall contain only alphabets')
    email_validator = EmailValidator(message='Please check the email address')
    # Regex Reference : https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
    phone_validator = RegexValidator(
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
        'Please check your phone number')

    owner_id= models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, validators=[alphabet_validator])
    last_name = models.CharField(max_length=50, validators=[alphabet_validator])
    email = models.EmailField(max_length=100, validators=[email_validator])
    phone = models.CharField(max_length=20, validators=[phone_validator])
    password = models.CharField(max_length=20, validators=[alphanumeric_validator])