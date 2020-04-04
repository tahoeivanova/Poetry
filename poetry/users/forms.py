# from django import forms
from .models import PoemsUser
from django.contrib.auth.forms import UserCreationForm

class RegistrationUserForm(UserCreationForm):

    class Meta:
        model = PoemsUser
        fields = ('username', 'password', 'email')
