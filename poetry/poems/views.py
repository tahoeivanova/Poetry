from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Poem
from .forms import PoemForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .AudioPoet import AudioPoet


class PoemView(ListView):
    model = Poem
    template_name = 'poems/poems.html'
    context_object_name = 'poem'


class ContentsView(ListView):
    model = Poem
    template_name = 'poems/contents.html'
    context_object_name = 'poem'


class PoemUpdateView(UpdateView):
    model = Poem
    template_name = 'poems/poem_update.html'
    fields = '__all__'
    success_url = reverse_lazy('poems:poems')


@user_passes_test(lambda user: user.is_superuser)
def poem_add(request):
    if request.method == "GET":
        form = PoemForm
        return render(request, 'poems/poem_add.html', {'form': form})
    else:
        form = PoemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('poems:poems'))
        else:
            return render(request, 'poems/poem_add.html', {'form': form})

class PoemDetailView(DetailView):
    model = Poem
    template_name = 'poems/poem_single.html'

class PoemDeleteView(UserPassesTestMixin, DeleteView):

    template_name = 'poems/poem_delete.html'
    model = Poem
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('home'))

def audio_poem(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    title = poem.poem_title
    text = str(poem.poem_text)
    a = AudioPoet(text)
    a.audio()
    return render(request, 'poems/poem_audio.html', {'title': title})