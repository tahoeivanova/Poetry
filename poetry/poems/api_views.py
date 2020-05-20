from .models import Tag, Poem
from .serializer import TagSerializer, PoemSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PoemPushkinViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.prefetch_related('poem_tag').filter(poet_name__last_name='Пушкин')
    serializer_class = PoemSerializer

class PoemLermontovViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.prefetch_related('poem_tag').filter(poet_name__last_name='Лермонтов')
    serializer_class = PoemSerializer

class PoemAkhmadulinaViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.prefetch_related('poem_tag').filter(poet_name__last_name='Ахмадулина')
    serializer_class = PoemSerializer