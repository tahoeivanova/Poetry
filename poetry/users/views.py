from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import RegistrationUserForm
from .models import PoemsUser
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserCreateView(CreateView):
    model = PoemsUser
    template_name = 'users/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('home')
