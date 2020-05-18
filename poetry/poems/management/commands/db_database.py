from django.core.management.base import BaseCommand
from poems.models import Poem, Tag, Poet
import re
import pandas as pd




class Command(BaseCommand):
    def handle(self, *args, **options):
        # 1_______Добавление автора________on_delete=models.Cascade
        # ВЫПОЛНЕНО
        # p = Poet.objects.create(last_name='Ахмадулина', first_name='Белла', father_name='Ахатовна')
        # print(Poet.objects.first())

        # 1.1_______Добавление автора________
        # ВЫПОЛНЕНО
        # poet = Poet.objects.get(last_name='Пушкин', first_name='Александр', father_name='Сергеевич')
        # print(poet)

        # 2.1________Добавление в базу данных из csv при помощи pandas________
        # ВЫПОЛНЕНО

        # poet = Poet.objects.get(last_name="Ахмадулина")
        # # # print(poet)
        # data = pd.read_csv('poems/df_Akhmadulina.csv', sep=',')
        # for _, row in data.iterrows():
        #     Poem.objects.create(poem_title=row['Название'], poem_text=row['Текст'], poet_name=poet)

        # 2.2________Добавление в базу данных из csv при помощи pandas________
        # ВЫПОЛНЕНО
        # poet = Poet.objects.get(last_name='Лермонтов', first_name='Михаил', father_name='Юрьевич')
        # #
        # data = pd.read_csv('poems/df_Lermontov.csv', sep=',')
        # for _, row in data.iterrows():
        #     Poem.objects.create(poem_title=row['Название'], poem_text=row['Текст'], poem_year=row['Год'], poet_name=poet)

        # 3________Изменение поля poem_year с nan на пробел________
        # ВЫПОЛНЕНО
        # poems = Poem.objects.filter(poem_year='nan')
        # for poem in poems:
        #     poem.poem_year = ''
        #     poem.save()
        #     print(poem, poem.poem_year)

        # 4________Добавление первой строки в объект базы данных________
        # ВЫПОЛНЕНО
        # poems = Poem.objects.filter(poet_name__last_name="Ахмадулина")
        # for one_poem in poems:
        #     text = one_poem.poem_text
        #     str_list = text.split('\n')
        #     str_add = str_list[3]
        #     # print(str_add)
        #     str_add = re.sub(r'[:;, *-]*$','...', str_add)
        #     one_poem.first_line = str_add
        #
        #     one_poem.save()
        # # ______________________

        # ___________1 функция из .models
        # poems = Poem.objects.all()
        # for poem in poems:
        #     print(poem.poem_no_name())

        # ___________2 функция из .models
        # for poem in poems:
        #     print(poem.tag_is())

        # ________Удаление всех объектов из базы данных________

        # poems = Poem.objects.all()
        # for p in poems:
        #     p.delete()

        # ________Удаление стихов одного поэта________

        # poems = Poem.objects.filter(poet_name__last_name='Ахмадулина')
        # for p in poems:
        #     p.delete()



