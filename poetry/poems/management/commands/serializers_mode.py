from django.core.management.base import BaseCommand
from poems.models import Poet, Poem
from poems.serializer import PoemSerializer,EmelyanovaPoemSerializer



class Command(BaseCommand):
    def handle(self, *args, ** options):
        serializer = PoemSerializer()
        print(repr(serializer))



