#Reference : https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator,EmailValidator
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	alphanumeric_validator = RegexValidator(r'^[A-Za-z0-9]*$','Shall Contain only alphabets and numbers')
	alphabet_validator = RegexValidator(r'^[A-Za-z0-9]$','Shall contain only alphabets')
	email_validator = EmailValidator(message = 'Please check the email address')
    # Regex Reference : https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
	phone_validator = RegexValidator(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})','Please check your phone number')
	numeric_validator = RegexValidator(r'^[0-9]*$','Shall contain only numbers')
	gender_validator = RegexValidator(r'^[M|F|O|N]$','Enter a valid gender')
    
	first_name = forms.CharField(max_length=50,validators=[alphanumeric_validator])
	last_name = forms.CharField(max_length=50,validators=[alphanumeric_validator])
	gender = forms.CharField(max_length=1, validators=[gender_validator])
	email = forms.EmailField(max_length=100,validators=[email_validator])
	phone = forms.CharField(max_length=20,validators=[phone_validator])
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone','gender',)

