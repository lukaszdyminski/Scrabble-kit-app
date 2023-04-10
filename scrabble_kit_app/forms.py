from .models import *
from django.forms import ModelForm
from django import forms


# user enters in here amount of tiles both hidden ones and from the board
class ScrabbleWordLengthForm(ModelForm):

    class Meta:
        model = ScrabbleWordLength
        fields = ('user_word_length', 'board_tiles')


# user enters in here his/her own hidden tiles
class UserScrabbleSetForm(ModelForm):

    class Meta:
        model = UserScrabbleSet
        fields = ('user_tile', )
        widgets = {'user_tile': forms.TextInput(attrs={'required': True})}

    # method transforming lowercase tile letter from user into uppercase one
    def clean_user_tile(self):
        return self.cleaned_data['user_tile'].upper()


# user enters in here the tiles from the board
class BoardScrabbleSetForm(ModelForm):

    class Meta:
        model = BoardScrabbleSet
        fields = ('board_tile', )
        widgets = {'board_tile': forms.TextInput(attrs={'required': True})}

    # method transforming lowercase tile letter from the board into uppercase one
    def clean_board_tile(self):
        return self.cleaned_data['board_tile'].upper()
