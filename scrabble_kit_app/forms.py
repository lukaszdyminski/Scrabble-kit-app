from .models import *
from django.forms import ModelForm
from django import forms


class ScrabbleWordLengthForm(ModelForm):

    class Meta:
        model = ScrabbleWordLength
        fields = ('user_word_length', 'board_tiles')


class UserScrabbleSetForm(ModelForm):

    class Meta:
        model = UserScrabbleSet
        fields = ('user_tile', )
        widgets = {'user_tile': forms.TextInput(attrs={'required': True})}

    def clean_user_tile(self):
        return self.cleaned_data['user_tile'].upper()


class BoardScrabbleSetForm(ModelForm):

    class Meta:
        model = BoardScrabbleSet
        fields = ('board_tile', )
        widgets = {'board_tile': forms.TextInput(attrs={'required': True})}

    def clean_board_tile(self):
        return self.cleaned_data['board_tile'].upper()
