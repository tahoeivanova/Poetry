from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from poems.models import Poem, Poet



def home_page(request):
    poems = Poem.emelyanova.all()
    poet = poems[0].poet_name

    return render(request, 'poems/index.html', {'poet': poet, 'poems':poems})

