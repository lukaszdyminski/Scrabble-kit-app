# Generated by Django 4.0.1 on 2023-03-26 21:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrabble_kit_app', '0009_boardscrabbleset_userscrabbleset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardscrabbleset',
            name='board_tile',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')]),
        ),
    ]