# Generated by Django 4.0.1 on 2022-07-13 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrabble_kit_app', '0004_remove_scrabbleset_tile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrabbleset',
            name='tile_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrabble_kit_app.scrabblewordlength'),
        ),
    ]
