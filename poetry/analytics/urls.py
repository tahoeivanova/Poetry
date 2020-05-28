"""poetry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'analytics'

urlpatterns = [
    path('options/<poet>/', views.checkbox_dictionary, name='analytics_main'),
    path('dictionary/<int:pk>/', views.poem_dictionary, name='pd'),
    path('all_words_counted/<poet>/', views.all_words_counted, name='all_words_counted'),
    path('top_100_nouns/<poet>/', views.top_100_nouns, name='top_100_nouns'),
    path('top_100_adjf/<poet>/', views.top_100_adjf, name='top_100_adjf'),
    path('top_100_nouns_and_adjf/<poet>/', views.top_100_nouns_and_adjf, name='top_100_nouns_and_adjf'),
    path('top_100_verbs/<poet>/', views.top_100_verbs, name='top_100_verbs'),
    path('top_100_nouns_and_verbs/<poet>/', views.top_100_nouns_and_verbs, name='top_100_nouns_and_verbs'),
    path('top_100_nouns_and_verbs_and_adjf/<poet>/', views.top_100_nouns_and_verbs_and_adjf, name='top_100_nouns_and_verbs_and_adjf'),
    path('top_100_verbs_and_adjf/<poet>/', views.top_100_verbs_and_adjf, name='top_100_verbs_and_adjf'),


]
