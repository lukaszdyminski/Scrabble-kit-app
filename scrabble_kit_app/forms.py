from .models import *
from django.forms import ModelForm


class ScrabbleWordLengthForm(ModelForm):

    class Meta:
        model = ScrabbleWordLength
        fields = ('word_length',)


class ScrabbleSetForm(ModelForm):

    class Meta:
        model = ScrabbleSet
        fields = ('tile',)

    def clean_tile(self):
        return self.cleaned_data['tile'].upper()
