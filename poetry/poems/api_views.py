from .models import Tag, Poem, Poet
from .serializer import TagSerializer, PoemSerializer, EmelyanovaPoemSerializer, PoetSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly, IsAuthenticated_CUSTOM
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication



# ViewSets define the view behavior.
class PoetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Poet.poets.all()
    serializer_class = PoetSerializer

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated_CUSTOM | ReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class EmelyanovaPoemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = Poem.emelyanova.prefetch_related('poem_tag', 'poet_name').all()
    serializer_class = EmelyanovaPoemSerializer


class PoemPushkinViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Poem.objects.prefetch_related('poem_tag', 'poet_name').filter(poet_name__last_name='Пушкин')
    serializer_class = PoemSerializer

class PoemLermontovViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Poem.objects.prefetch_related('poem_tag', 'poet_name').filter(poet_name__last_name='Лермонтов')
    serializer_class = PoemSerializer

class PoemAkhmadulinaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    queryset = Poem.objects.prefetch_related('poem_tag', 'poet_name').filter(poet_name__last_name='Ахмадулина')
    serializer_class = PoemSerializer