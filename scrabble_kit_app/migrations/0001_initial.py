# Generated by Django 4.0.1 on 2022-06-26 14:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrabbleTiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_tiles_set', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrabbleWordLength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_length', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2, 'Min. value to enter is 2'), django.core.validators.MaxValueValidator(10, 'Max. value to enter is 10')])),
            ],
        ),
        migrations.CreateModel(
            name='ScrabbleSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile', models.CharField(max_length=10)),
                ('tile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scrabble_kit_app.scrabblewordlength')),
            ],
        ),
    ]