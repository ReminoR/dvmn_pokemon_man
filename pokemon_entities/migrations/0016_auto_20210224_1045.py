# Generated by Django 3.1.6 on 2021-02-24 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_delete_pokemonentity_temp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='pokemon',
            new_name='Pokemon',
        ),
    ]
