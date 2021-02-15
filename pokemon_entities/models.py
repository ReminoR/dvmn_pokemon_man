from django.db import models

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, null=True, blank=True)
    title_jp = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(default='Описание покемона')
    image = models.ImageField(upload_to='pokemons', null=True, blank=True)
    previous_evolution = models.ForeignKey('Pokemon', related_name = 'previous',null=True, blank=True, on_delete=models.SET_NULL)
    next_evolution = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lon = models.FloatField()
    lat = models.FloatField()
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()

    def __str__(self):
        return f"{self.lat} {self.lon}"

