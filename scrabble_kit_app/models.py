from django.db import models
from jsonfield import JSONField
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.translation import gettext_lazy


'''original full scrabble set model; sending to database 27 pairs "letter: letter-tiles-amount"
as the separate objects'''


class ScrabbleTiles(models.Model):
    all_tiles_set = JSONField()


'''user tiles amount model; sending to database number of tiles user needs to create a word, 
both the ones kept secret and the ones from the board'''


class ScrabbleWordLength(models.Model):
    user_word_length = models.IntegerField(null=True,
                                           validators=[MinValueValidator(2, gettext_lazy('Min. value to enter is 2')),
                                                       MaxValueValidator(7, gettext_lazy('Max. value to enter is 7'))])

    board_tiles = models.IntegerField(null=True,
                                      validators=[MinValueValidator(0, gettext_lazy('Min. value to enter is 0'))])

    def __str__(self):
        return "User letters amount is: {} -- Board letters amount is: {}".format(self.user_word_length,
                                                                                  self.board_tiles)


'''user tiles kept secret model; sending to database user tiles in the given amount'''

validate_user_tile = RegexValidator(r'^[a-zA-Z-]*$', 'Only letters and special character "-" are allowed.')


class UserScrabbleSet(models.Model):
    user_tile = models.CharField(max_length=1, validators=[validate_user_tile], blank=False)
    user_tile_id = models.ForeignKey(ScrabbleWordLength, on_delete=models.CASCADE, null=True,
                                     related_name='user_tile_rel')


'''board tiles model; sending to database tiles from the game board in the given amount'''

validate_board_tile = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')


class BoardScrabbleSet(models.Model):
    board_tile = models.CharField(max_length=1, validators=[validate_board_tile], blank=False)
    board_tile_id = models.ForeignKey(ScrabbleWordLength, on_delete=models.CASCADE, null=True,
                                      related_name='board_tile_rel')
