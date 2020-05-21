from django.conf.urls import url, include
from .models import Tag, Poem, Poet
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.

class PoetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poet
        fields = '__all__'

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PoemSerializer(serializers.HyperlinkedModelSerializer):

    poem_tag = serializers.StringRelatedField(many=True)
    poet_name = serializers.StringRelatedField(many=False)

    class Meta:
        model = Poem
        # exclude = ['url']
        fields = ['pk', 'poet_name', 'poem_title', 'poem_text', 'poem_year', 'poem_tag', ]
        # extra_kwargs = {
        #     'url': {'view_name': 'poem-detail', 'lookup_field': 'pk'},
        # }


class EmelyanovaPoemSerializer(serializers.HyperlinkedModelSerializer):
    poem_tag = serializers.StringRelatedField(many=True)
    poet_name = serializers.StringRelatedField(many=False)
    class Meta:
        model = Poem
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'poem-detail', 'lookup_field': 'pk'},
        }


