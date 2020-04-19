from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from poems.models import Poem, Poet



def home_page(request):
    poets = Poet.objects.all()
    return render(request, 'poems/index.html', {'poets': poets})

