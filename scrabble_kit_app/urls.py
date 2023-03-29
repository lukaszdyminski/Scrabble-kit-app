from django.urls import path
from .views import *

urlpatterns = [
    # home url displaying original full scrabble set and app short description
    path('home/', display_tiles_set, name='letters_dict'),

    # url where user enters letters amount of user's scrabble set
    path('letters_amount/', enter_letters_amount, name='letters_amount'),

    # url where user enters all tiles of user's scrabble set + tiles of the board to merge with
    path('your_scrabble_set/<int:pk>/', enter_user_scrabble_set, name='enter_user_scrabble_set'),

    # url displaying user tiles set from which the valid words will be formed
    path('your_scrabble_set/<int:pk>/your_scrabble_set_results/', display_user_scrabble_set,
         name='display_user_scrabble_set'),

    # url displaying valid words formed from user scrabble set
    path('your_scrabble_set/<int:pk>/scrabble_words_list/', display_words_list, name='display_words_list'),
]
