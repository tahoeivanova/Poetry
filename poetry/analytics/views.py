from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, HttpResponseRedirect, reverse
from poems.models import Poem, Poet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import collections, pymorphy2
from .PoetAnalytics import MetaPoet, words_counter, top_100
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import DictionaryFormPartOfSpeech



# подсчет числа слов всего, уникальных слов, топ 100 слов
def all_words_counted(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все cтихи одного поэта
    poems_all, counter_all, counter_unique, result, results_list_words,  results_list_counts = words_counter(poems)
    return render(request, 'analytics/poet_analytics.html', {'poet':poet, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique, 'result':result,'results_list_words':results_list_words, 'results_list_counts': results_list_counts})


def poem_dictionary(request, pk):
    poem_original = get_object_or_404(Poem, pk=pk)
    poem = str(poem_original.poem_text)
    meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
    meta_poem.remove_punctuation()
    meta_poem.split_words()
    meta_poem.lower_case()
    lemmed_words = meta_poem.lemma()  # список всех лемматизированных слов
    len_lemmed_words = len(lemmed_words)
    unique_words_list = meta_poem.unique_words()
    len_unique_words = len(unique_words_list)
    word_list_poem = meta_poem.poem_dictionary()
    return render(request, 'analytics/poem_dictionary.html', {'pk':pk, 'len_unique_words':len_unique_words,'len_lemmed_words':len_lemmed_words,'poem': word_list_poem, 'poem_original': poem_original})


def checkbox_dictionary(request, poet):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = DictionaryFormPartOfSpeech(request.POST)
        if form.is_valid():
            is_noun = form.cleaned_data['is_noun']
            is_adjf = form.cleaned_data['is_adjf']
            is_verb = form.cleaned_data['is_verb']

            # NOUN
            if is_noun==True and is_adjf==False and is_verb==False:
                return HttpResponseRedirect(reverse('analytics:top_100_nouns', args=(poet,)))
            # ADJF
            if is_noun==False and is_adjf==True and is_verb==False:
                return HttpResponseRedirect(reverse('analytics:top_100_adjf', args=(poet,)))
            #VERB
            if is_noun==False and is_adjf==False and is_verb==True:
                return HttpResponseRedirect(reverse('analytics:top_100_verbs', args=(poet,)))
            # NOUN AND ADJF
            if is_noun==True and is_adjf==True and is_verb==False:
                return HttpResponseRedirect(reverse('analytics:top_100_nouns_and_adjf', args=(poet,)))


            if is_noun == True and is_adjf == False and is_verb == True:
                return HttpResponseRedirect(reverse('analytics:top_100_nouns_and_verbs', args=(poet,)))
            if is_verb and is_noun==True and is_adjf==True:
                return HttpResponseRedirect(reverse('analytics:top_100_nouns_and_verbs_and_adjf', args=(poet,)))
            if is_verb and is_noun==False and is_adjf==True:
                return HttpResponseRedirect(reverse('analytics:top_100_verbs_and_adjf', args=(poet,)))
            else:
                return all_words_counted(request, poet)
    else:
        form = DictionaryFormPartOfSpeech()

        return render(request, 'analytics/checkbox.html', {'form': form, 'poet':poet})

# топ-100 по частям речи

def top_100_nouns(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all, counter_all, counter_unique, all_lemmed_words = top_100(poems)
    result = all_lemmed_words.top_100_nouns()
    return render(request, 'analytics/top_100_nouns.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})


def top_100_adjf(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet)
    poems_all, counter_all, counter_unique, all_lemmed_words = top_100(poems)
    result = all_lemmed_words.top_100_adjf()
    return render(request, 'analytics/top_100_adjf.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_nouns_and_adjf(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all, counter_all, counter_unique, all_lemmed_words = top_100(poems)
    result = all_lemmed_words.top_100_nouns_and_adjf()
    return render(request, 'analytics/top_100_nouns_and_adjf.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})


def top_100_verbs(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all, counter_all, counter_unique, all_lemmed_words = top_100(poems)
    result = all_lemmed_words.top_100_verbs()
    return render(request, 'analytics/top_100_verbs.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_nouns_and_verbs(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all, counter_all, counter_unique, all_lemmed_words = top_100(poems)
    result = all_lemmed_words.top_100_nouns_and_verbs()
    return render(request, 'analytics/top_100_nouns_and_verbs.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_nouns_and_verbs_and_adjf(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all, counter_all, counter_unique, all_lemmed_words = top_100(poems)
    result = all_lemmed_words.top_100_nouns_and_verbs_and_adjf()
    return render(request, 'analytics/top_100_nouns_and_verbs_and_adjf.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_verbs_and_adjf(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all, counter_all, counter_unique, all_lemmed_words = top_100(poems)
    result = all_lemmed_words.top_100_verbs_and_adjf()
    return render(request, 'analytics/top_100_verbs_and_adjf.html', {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})



