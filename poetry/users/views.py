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
        return render(request, 'users/get_token.html') # кнопка "Получить токен"
    else:
        token = Token.objects.get_or_create(user=request.user) # Нажимаем на кнопку, попадаем на страницу с токеном
        return render(request, 'users/token.html', {'user': request.user, 'email': request.user.email, 'token':token[0]})

def update_token(request):
    if request.method == 'GET':
        return render(request, 'users/token.html', {'user': request.user, 'token': 'Новый токен'})
    else:
        token = Token.objects.filter(user=request.user)
        new_key = token[0].generate_key()
        token.update(key=new_key)
        return render(request, 'users/token.html', {'user': request.user, 'email': request.user.email, 'token':token[0]})



