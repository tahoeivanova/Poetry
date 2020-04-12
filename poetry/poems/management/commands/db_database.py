from django.core.management.base import BaseCommand
from poems.models import Poem, Tag
import re
import pandas as pd




class Command(BaseCommand):
    def handle(self, *args, **options):
        #___________1 функция из .models
        poems = Poem.objects.all()
        # for poem in poems:
        #     print(poem.poem_no_name())

        #___________2 функция из .models
        # for poem in poems:
        #     print(poem.tag_is())


        # _______Добавление автора________on_delete=models.Cascade
        # p = Poet.objects.create(last_name='Пушкин', first_name='Александр', father_name='Сергеевич')
        # p.save()


# ________Удаление всех объектов из базы данных________

         # poems = Poem.objects.all()
         # for p in poems:
         #     p.delete()




# ________Добавление в базу данных из csv при помощи pandas________


         # data = pd.read_csv('poems/df_1.csv', sep = ',')
         # for _, row in data.iterrows():
         #     Poem.objects.create(poem_title = row['Название'], poem_text = row['Текст'])

# ________Добавление первой строки в объект базы данных________
#
        # poems = Poem.objects.filter(poem_title='* * *')
        #
        #
        # for one_poem in poems:
        #     text = one_poem.poem_text
        #     str_list = text.split('\n')
        #     str_add = str_list[3]
        #     str_add = re.sub(r'[.:, .*-]*$','...', str_add)
        #     one_poem.first_line = str_add
        #
        #     one_poem.save()
#______________________



