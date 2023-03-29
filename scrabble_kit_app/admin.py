from django.contrib import admin
from scrabble_kit_app.models import *

# Register your models here.


@admin.register(ScrabbleTiles)
class ScrabbleTiles(admin.ModelAdmin):
    pass


@admin.register(ScrabbleWordLength)
class ScrabbleWordLength(admin.ModelAdmin):
    pass


@admin.register(UserScrabbleSet)
class UserScrabbleSet(admin.ModelAdmin):
    pass


@admin.register(BoardScrabbleSet)
class BoardScrabbleSet(admin.ModelAdmin):
    pass
