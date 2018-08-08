from django import forms
from authorize.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

