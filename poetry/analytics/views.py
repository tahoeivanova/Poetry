from django.shortcuts import render
from django.shortcuts import render
from poems.models import Poem
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import collections, pymorphy2
from .PoetAnalytics import MetaPoet


# Create your views here.

# подсчет числа слов всего, уникальных слов, топ 100 слов
def all_words_counted(request):
    poems = Poem.objects.all() # все объекты класса Стихи
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
    # список топ 100 из существительных и глаголов
    lemmed_words = [word for word in lemmed_words if morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'INFN' or morph.parse(word)[0].tag.POS == 'ADJF' or morph.parse(word)[0].tag.POS == 'ADJS' or morph.parse(word)[0].tag.POS == 'PRTF' or morph.parse(word)[0].tag.POS == 'GRND' or morph.parse(word)[0].tag.POS == 'ADVB']


    c = collections.Counter(lemmed_words)
    result = c.most_common(100)

    #  вывод кортежа

    # преобразовываем список кортежей в список (убираем цифры, который обозначают частоту встречаемости)

    results_list_words = []
    results_list_counts = []

    for tuple_ in result:
        for i in range(len(tuple_)):
            if i == 0:
                results_list_words.append(tuple_[i])
            if i == 1:
                results_list_counts.append(tuple_[i])



    return render(request, 'analytics/poet_analytics.html', {'poems_all':poems_all,'result':result,'results_list_words':results_list_words, 'results_list_counts': results_list_counts,'counter_all': counter_all,'counter_unique':counter_unique})

