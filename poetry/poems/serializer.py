from django.conf.urls import url, include
from .models import Tag, Poem, Poet
from rest_framework import routers, serializers, viewsets


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class EmelyanovaPoemSerializer(serializers.HyperlinkedModelSerializer):
    poem_tag = serializers.StringRelatedField(many=True)
    poet_name = serializers.StringRelatedField(many=False)
    class Meta:
        model = Poem
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'poem-detail', 'lookup_field': 'pk'},
        }


