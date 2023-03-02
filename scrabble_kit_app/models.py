from django.db import models
from jsonfield import JSONField
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.translation import gettext_lazy


class ScrabbleTiles(models.Model):
    all_tiles_set = JSONField()


class ScrabbleWordLength(models.Model):
    word_length = models.IntegerField(null=True,
                                      validators=[MinValueValidator(2, gettext_lazy('Min. value to enter is 2')),
                                                  MaxValueValidator(10, gettext_lazy('Max. value to enter is 10'))])

    def __str__(self):
        return "Letters amount is: {}".format(self.word_length)


validate_tile = RegexValidator(r'^[a-zA-Z-]*$', 'Only letters and special character "-" are allowed.')


class ScrabbleSet(models.Model):
    tile = models.CharField(max_length=1, validators=[validate_tile])
    tile_id = models.ForeignKey(ScrabbleWordLength, on_delete=models.CASCADE, null=True, related_name='tiles_set')

