from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import RegistrationUserForm
from .models import PoemsUser
from rest_framework.authtoken.models import Token
from users.models import CustomAuthToken
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserCreateView(CreateView):
    model = PoemsUser
    template_name = 'users/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('home')

def get_token(request):
    if request.method == 'GET':
        return render(request, 'users/get_token.html')
    else:
        token = Token.objects.get_or_create(user=request.user)
        return render(request, 'users/token.html', {'user': request.user, 'token':token[0]})



