from django import forms
from .models import Poem

class PoemForm(forms.ModelForm):
    poem_title = forms.CharField(label = 'Название')


    class Meta:
        model = Poem
        # fields = '__all__'
        exclude = ['poem_audio','poem_img']