from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Poem, Poet
from .forms import PoemForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .AudioPoet import AudioPoet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# все стихи всех поэтов
class PoemView(ListView):
    model = Poem
    template_name = 'poems/poems.html'
    context_object_name = 'poem'
    paginate_by = 10

# стихи одного автора

def poems_author(request, poet):
    poem = Poem.objects.prefetch_related('poem_tag').filter(poet_name__last_name=poet).filter(is_active=True)
    paginator = Paginator(poem, 15)  # Show 15 contacts per page.
    page = request.GET.get('page')
    try:
        poem = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        poem = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        poem = paginator.page(paginator.num_pages)

    return render(request, 'poems/poems_author.html', {'poem': poem, 'p_':poem[0]})



class ContentsView(ListView):
    model = Poem
    template_name = 'poems/contents.html'
    context_object_name = 'poem'

    def get_queryset(self):
        return Poem.objects.filter(is_active=True)

# содержание по одному автору

def contents_author(request, poet):
    poem = Poem.objects.filter(poet_name__last_name=poet)
    return render(request, 'poems/contents_author.html', {'poem':poem})


class PoemUpdateView(UpdateView):
    model = Poem
    template_name = 'poems/poem_update.html'
    fields = ['is_active','poem_title', 'poem_text', 'poem_year', 'first_line', 'poem_tag', 'poet_name']
    success_url = reverse_lazy('home')


@user_passes_test(lambda user: user.is_superuser)
def poem_add(request):
    if request.method == "GET":
        form = PoemForm
        return render(request, 'poems/poem_add.html', {'form': form})
    else:
        form = PoemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
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
    text = str(poem.poem_text)
    a = AudioPoet(text)
    a.audio()
    poem.poem_audio = 'poems/audio/1.mp3'
    poem.save()

    return render(request, 'poems/poem_audio.html', {'poem': poem})