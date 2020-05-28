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


app_name = 'poems'

urlpatterns = [
    path('poet/<poet>', views.poems_author, name='poems_author'),
    path('contents/<poet>', views.contents_author, name='contents_author'),
    path('add/', views.poem_add, name='poem_add'),
    path('poem_single/<int:pk>/', views.PoemDetailView.as_view(), name='poem_single'),
    path('delete/<int:pk>/', views.PoemDeleteView.as_view(), name='poem_delete'),
    path('contents/', views.ContentsView.as_view(), name='contents'),
    path('audio/<int:pk>/', views.audio_poem, name='audio'),
    path('update/<int:pk>/', views.PoemUpdateView.as_view(), name='poem_update'),
]

