from rest_framework import serializers
from .models import *


class ScrabbleTilesSerializer(serializers.ModelSerializer):
    all_tiles_set = serializers.JSONField(required=False)

    class Meta:
        model = ScrabbleTiles
        fields = ['all_tiles_set', ]


class ScrabbleWordLengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrabbleWordLength
        fields = ['word_length', ]


class ScrabbleSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScrabbleSet
        fields = ['user_tile', 'tile_id']
