from django.db import models
from django.core.validators import RegexValidator,EmailValidator


class User(models.Model):

    alphanumeric_validator = RegexValidator(r'^[A-Za-z0-9]*$','Shall Contain only alphabets and numbers')
    alphabet_validator = RegexValidator(r'^[A-Za-z]$','Shall contain only alphabets')
    numeric_validator = RegexValidator(r'^[0-9]$','Shall contain only numerals')
    email_validator = EmailValidator(message='Please check the email address')

    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=400,validators=[email_validator])
    user_password = models.CharField(max_length=400)
    user_cpassword = models.CharField(max_length=400)
    user_dob = models.CharField(max_length=10)
    user_country = models.CharField(max_length=50)

    # def __init__(self, name=None, email=None, password=None,
    #              cpassword=None, dob=None, country=None ):
    #     self.name = name
    #     self.email = email
    #     self.password = password
    #     self.cpassword = cpassword
    #     self.dob = dob
    #     self.country = country
    #
    # def parse_user(self, register_form):
    #     self.name = register_form['name']
    #     self.email = register_form['email']
    #     self.password = register_form['password']
    #     self.cpassword = register_form['cpassword']
    #     hasher = PasswordHasher()
    #     self.password = hasher.hash(self.password)
    #     self.cpassword = hasher.hash(self.cpassword)
    #     self.dob = register_form['dob']
    #     self.country = register_form['country']
