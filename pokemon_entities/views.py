import folium
import json
import os

from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # tooltip=name,  # disable tooltip because of folium encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    # with open("pokemon_entities/pokemons.json", encoding="utf-8") as database:
    #     pokemons = json.load(database)['pokemons']
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in PokemonEntity.objects.filter(Pokemon = pokemon):
            add_pokemon(
                folium_map, 
                pokemon_entity.lat, 
                pokemon_entity.lon, 
                request.build_absolute_uri(pokemon.image.url))

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url),
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    # with open("pokemon_entities/pokemons.json", encoding="utf-8") as database:
    #     pokemons = json.load(database)['pokemons']
    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = pokemon
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    pokemons_entities = PokemonEntity.objects.filter(Pokemon=requested_pokemon)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon, request.build_absolute_uri(requested_pokemon.image.url))

    pokemon = {
        "pokemon_id": requested_pokemon.id,
        "title_ru": requested_pokemon.title,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
        "description": requested_pokemon.description,
        "img_url": request.build_absolute_uri(requested_pokemon.image.url),
    }

    try:
        pokemon["previous_evolution"] = {
            "title_ru": requested_pokemon.previous_evolution.title,
            "pokemon_id": requested_pokemon.previous_evolution.id,
            "img_url": requested_pokemon.previous_evolution.image.url
        }
    except AttributeError:
        pass

    try:
        pokemon["next_evolution"] = {
            "title_ru": requested_pokemon.next_evolution.title,
            "pokemon_id": requested_pokemon.next_evolution.id,
            "img_url": requested_pokemon.next_evolution.image.url
        }
    except AttributeError:
        pass

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
