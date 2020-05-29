from django.core.management.base import BaseCommand
from poems.models import Poet, Poem
import json
import pprint



class Command(BaseCommand):
    def handle(self, *args, ** options):

        # создать имя/фамилию поэта
        # ВЫПОЛНЕНО
        Poet.poets.create(last_name="Емельянова", first_name="Клара" )


        # запросить поэта, задать кастомный номер 1
        # ВЫПОЛНЕНО

        poet = Poet.poets.get(last_name="Емельянова")
        poet.custom_id=1
        poet.save()


        # Загрузить стихи из файла json
        # ВЫПОЛНЕНО
        with open('poems/poems_by_lera.json') as f:
            data = json.load(f)

        poet_name = Poet.objects.get(custom_id=1)
        for row in data:
            Poem.objects.create(poem_title=row['poem_title'], poem_text=row['poem_text'], first_line=row['first_line'], poet_name=poet_name)
