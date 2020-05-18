from django.core.management.base import BaseCommand
from poems.models import Poem, Tag, Poet
from poetry.analytics.models import AnalyticsInfo
from analytics.PoetAnalytics import MetaPoet
import re
import pandas as pd




class Command(BaseCommand):
    def handle(self, *args, **options):

        dict_words = dict.fromkeys(['Количество стихов', 'Все слова (лемматизированные)', 'Уникальные слова', 'Количество всех слов', 'Количество уникальных слов'])

        poems = Poem.objects.filter(poet_name__last_name='Ахмадулина')
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