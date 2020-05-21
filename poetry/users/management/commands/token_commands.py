from django.core.management.base import BaseCommand
from users.models import PoemsUser
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    def handle(self, *args, **options):
        # for user in PoemsUser.objects.all():
        #     token = Token.objects.get_or_create(user=user)
        #     print(user, token)
        print(dir(PoemsUser))
        # token = Token.objects.create(user='eliot')
