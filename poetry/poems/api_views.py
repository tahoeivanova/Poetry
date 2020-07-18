from .models import Tag, Poem, Poet
from .serializer import TagSerializer, EmelyanovaPoemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly, IsAuthenticated_CUSTOM
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication




class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class EmelyanovaPoemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = Poem.emelyanova.prefetch_related('poem_tag', 'poet_name').all()
    serializer_class = EmelyanovaPoemSerializer