from django.core.management.base import BaseCommand
from poems.models import Poet, Poem
import json
import pprint



class Command(BaseCommand):
    def handle(self, *args, ** options):
        # создать имя/фамилию поэта
        # ВЫПОЛНЕНО
        # Poet.objects.create(last_name="Емельянова", first_name="Клара" )


        # посмотреть файл json в терминале
        # ВЫПОЛНЕНО
        # with open('poems/poems_by_lera.json') as f:
        #     data = json.load(f)
        # print(type(data)) # класс list
        # pprint.pprint(data)
        # вывести первое название
        # print(data[0]['poem_title'])
        # print(len(data)) # 34 стиха


        # Загрузить стихи из файла json
        # в цикле
        # ВЫПОЛНЕНО

        # poet_name = Poet.objects.filter(last_name="Емельянова").first()
        # for row in data:
        #     Poem.objects.create(poem_title=row['poem_title'], poem_text=row['poem_text'], first_line=row['first_line'], poet_name=poet_name)
