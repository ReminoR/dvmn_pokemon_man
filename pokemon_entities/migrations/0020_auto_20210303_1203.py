# Generated by Django 3.1.7 on 2021-03-03 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0019_auto_20210303_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(related_name='pokemons', to='pokemon_entities.PokemonElementType'),
        ),
    ]