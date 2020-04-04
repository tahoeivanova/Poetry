from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from poems.models import Poem



def home_page(request):
    return render(request, 'poems/index.html')

