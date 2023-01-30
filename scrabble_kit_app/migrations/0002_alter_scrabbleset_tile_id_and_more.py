# Generated by Django 4.0.1 on 2022-06-26 14:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrabble_kit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrabbleset',
            name='tile_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrabble_kit_app.scrabblewordlength'),
        ),
        migrations.AlterField(
            model_name='scrabblewordlength',
            name='word_length',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(2, 'Min. value to enter is 2'), django.core.validators.MaxValueValidator(10, 'Max. value to enter is 10')]),
        ),
    ]