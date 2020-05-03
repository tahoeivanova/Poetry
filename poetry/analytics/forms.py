from django import forms
from .models import DictionaryForm

class DictionaryFormPartOfSpeech(forms.ModelForm):


    class Meta:
        model = DictionaryForm
        fields = ('is_noun', 'is_adjf', 'is_verb')


