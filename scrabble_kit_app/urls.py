from django.urls import path
from .views import *

urlpatterns = [
    path('home/', display_tiles_set, name='letters_dict'),
    path('letters_amount/', enter_letters_amount, name='letters_amount'),
    path('your_scrabble_set/<int:pk>/', enter_user_scrabble_set, name='enter_user_scrabble_set'),
    path('your_scrabble_set/<int:pk>/your_scrabble_set_results/', display_user_scrabble_set, name='display_user_scrabble_set'),
    path('your_scrabble_set/<int:pk>/scrabble_words_list/', display_words_list, name='display_words_list'),
]
