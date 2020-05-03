from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, HttpResponseRedirect, reverse
from poems.models import Poem, Poet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import collections, pymorphy2
from .PoetAnalytics import MetaPoet
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import DictionaryFormPartOfSpeech

# время выполнения функции

# Create your views here.

# подсчет числа слов всего, уникальных слов, топ 100 слов
def all_words_counted(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem) # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma() # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)


    morph = pymorphy2.MorphAnalyzer()
    # список топ 100 из существительных, глаголов и др
    lemmed_words = [word for word in lemmed_words if morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'INFN' or morph.parse(word)[0].tag.POS == 'ADJF' or morph.parse(word)[0].tag.POS == 'ADJS' or morph.parse(word)[0].tag.POS == 'PRTF' or morph.parse(word)[0].tag.POS == 'GRND' or morph.parse(word)[0].tag.POS == 'ADVB'or morph.parse(word)[0].tag.POS == 'NPRO']


    c = collections.Counter(lemmed_words)
    result = c.most_common(100)

    #  вывод кортежа

    # преобразовываем список кортежей в список (убираем цифры, который обозначают частоту встречаемости)

    results_list_words = []
    results_list_counts = [] # СЕЙЧАС СПИСКИ НЕ ИСПОЛЬЗУЮТСЯ
    # НУЖНО ДОДЕЛАТЬ И ПРОИТЕРИРОВАТЬ СЛОВАРЬ

    for tuple_ in result:
        for i in range(len(tuple_)):
            if i == 0:
                results_list_words.append(tuple_[i])
            if i == 1:
                results_list_counts.append(tuple_[i])



    return render(request, 'analytics/poet_analytics.html', {'poet':poet, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique, 'result':result,'results_list_words':results_list_words, 'results_list_counts': results_list_counts})


@login_required
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
    return render(request, 'analytics/poem_dictionary.html', {'len_unique_words':len_unique_words,'len_lemmed_words':len_lemmed_words,'poem': word_list_poem, 'poem_original': poem_original})


def checkbox_dictionary(request, poet):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = DictionaryFormPartOfSpeech(request.POST)

        # create a form instance and populate it with data from the request:
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

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DictionaryFormPartOfSpeech()

        return render(request, 'analytics/checkbox.html', {'form': form, 'poet':poet})

# топ-100 по частям речи

def top_100_words(request):
    poems = Poem.objects.all()  # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    m = MetaPoet(lemmed_words)
    result = m.top_100_words()
    return render(request, 'analytics/top_100_words.html',
                  {'result': result,'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_nouns(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    m = MetaPoet(lemmed_words)
    result = m.top_100_nouns()
    return render(request, 'analytics/top_100_nouns.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})


def top_100_adjf(request):
    poems = Poem.objects.all()  # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    m = MetaPoet(lemmed_words)
    result = m.top_100_adjf()
    return render(request, 'analytics/top_100_adjf.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_nouns_and_adjf(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    # poems = Poem.objects.all()  # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    m = MetaPoet(lemmed_words)
    result = m.top_100_nouns_and_adjf()
    return render(request, 'analytics/top_100_nouns_and_adjf.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})


def top_100_verbs(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    m = MetaPoet(lemmed_words)
    result = m.top_100_verbs()
    return render(request, 'analytics/top_100_verbs.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_nouns_and_verbs(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    m = MetaPoet(lemmed_words)
    result = m.top_100_nouns_and_verbs()
    return render(request, 'analytics/top_100_nouns_and_verbs.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_nouns_and_verbs_and_adjf(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    m = MetaPoet(lemmed_words)
    result = m.top_100_nouns_and_verbs_and_adjf()
    return render(request, 'analytics/top_100_nouns_and_verbs_and_adjf.html',
                      {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def top_100_verbs_and_adjf(request, poet):
    poems = Poem.objects.filter(poet_name__last_name=poet) # все объекты класса Стихи
    poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    m = MetaPoet(lemmed_words)
    result = m.top_100_verbs_and_adjf()
    return render(request, 'analytics/top_100_verbs_and_adjf.html', {'result': result, 'poems_all':poems_all,'counter_all': counter_all,'counter_unique':counter_unique})

def compare_poets_main(request):
    return render(request, 'analytics/analytics_main.html')



def compare_poets(request):
    poet1 = Poet.objects.get(last_name='Пушкин')
    poet2 = Poet.objects.get(last_name='Лермонтов')
    poems1 = Poem.objects.filter(poet_name__last_name='Пушкин')
    poems2 = Poem.objects.filter(poet_name__last_name='Лермонтов')  # все объекты класса Стихи

    # poems_all = len(poems)
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems1:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)

    morph = pymorphy2.MorphAnalyzer()
    # список топ 100 из существительных, глаголов и др
    lemmed_words = [word for word in lemmed_words if
                    morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'INFN' or
                    morph.parse(word)[0].tag.POS == 'ADJF' or morph.parse(word)[0].tag.POS == 'ADJS' or
                    morph.parse(word)[0].tag.POS == 'PRTF' or morph.parse(word)[0].tag.POS == 'GRND' or
                    morph.parse(word)[0].tag.POS == 'ADVB' or morph.parse(word)[0].tag.POS == 'NPRO']

    c = collections.Counter(lemmed_words)
    result1 = c.most_common(100)

    # counter_all
    results_list_words_1 = []
    results_list_counts_1 = []
    results_list_percent_1 = [] # СЕЙЧАС СПИСКИ НЕ ИСПОЛЬЗУЮТСЯ
    # НУЖНО ДОДЕЛАТЬ И ПРОИТЕРИРОВАТЬ СЛОВАРЬ

    for tuple_ in result1:
        for i in range(len(tuple_)):
            if i == 0:
                results_list_words_1.append(tuple_[i])
            if i == 1:
                results_percent = f'{round((tuple_[i]/counter_all*100),2)}%'
                results_list_percent_1.append(results_percent)
                results_list_counts_1.append(tuple_[i])


    for poem in poems2:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)

    morph = pymorphy2.MorphAnalyzer()
    # список топ 100 из существительных, глаголов и др
    lemmed_words = [word for word in lemmed_words if
                    morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'INFN' or
                    morph.parse(word)[0].tag.POS == 'ADJF' or morph.parse(word)[0].tag.POS == 'ADJS' or
                    morph.parse(word)[0].tag.POS == 'PRTF' or morph.parse(word)[0].tag.POS == 'GRND' or
                    morph.parse(word)[0].tag.POS == 'ADVB' or morph.parse(word)[0].tag.POS == 'NPRO']

    c = collections.Counter(lemmed_words)
    result2 = c.most_common(100)

    # counter_all
    results_list_words_2 = []
    results_list_counts_2 = []
    results_list_percent_2 = []

    for tuple_ in result2:
        for i in range(len(tuple_)):
            if i == 0:
                results_list_words_2.append(tuple_[i])
            if i == 1:
                results_percent = round((tuple_[i]/counter_all*100),2)
                results_list_percent_2.append(results_percent)
                results_list_counts_2.append(tuple_[i])

    result1 = zip(results_list_words_1, results_list_counts_1, results_list_percent_1)
    result2 = zip(results_list_words_2,results_list_counts_2, results_list_percent_2)

    return render(request, 'analytics/two_poets.html', {'result1': result1, 'result2': result2, 'poet1':poet1, 'poet2':poet2})
