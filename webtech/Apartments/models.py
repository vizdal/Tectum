from django.db import models
from django.core.validators import RegexValidator,EmailValidator
import json

# Create your models here.
class Apartment(models.Model):

    alphanumeric_validator = RegexValidator(r'^[A-Za-z0-9]*$','Shall Contain only alphabets and numbers')
    alphabet_validator = RegexValidator(r'^[A-Za-z0-9]$','Shall contain only alphabets')
    numeric_validator = RegexValidator(r'^[0-9]$','Shall contain only numerals')
    email_validator = EmailValidator(message='Please check the email address')

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

    posession = (
        ('<1', 'Less than month'),
        ('1-2', '1-2 month')
    )

    sharing = (

        ('Y','Sharing'),
        ('N', 'No-Sharing')

    )

    apartment_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey('owner',on_delete=models.CASCADE)
    apartment_name = models.CharField(max_length=50,validators=[alphanumeric_validator])
    # available_units = models.CharField(max_length=50, validators=[numeric_validator])
    apartment_location = models.CharField(max_length=400,validators=[alphanumeric_validator])
    apartment_description = models.CharField(max_length=400, validators=[alphanumeric_validator])
    apartment_price = models.CharField(max_length=50, validators=[numeric_validator])
    availability = models.CharField(max_length=1, choices=available_options)
    near_by = models.CharField(max_length=10, choices=near_by, default='DAL')
    type_of_room = models.CharField(max_length=10, choices=type_of_room,default='2')
    posession = models.CharField(max_length=10, choices=posession, default='<1')
    sharing = models.CharField(max_length=1, choices=sharing, default='Y')
    apartment_image = models.ImageField(upload_to='images/', default='images/svg/apartment8.jpg')

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