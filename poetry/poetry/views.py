from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from poems.models import Poem, Poet



def home_page(request):
    poet = Poet.objects.filter(last_name='Емельянова').first()

    return render(request, 'poems/index.html', {'poet': poet})

