from django.db import models

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemons', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lon = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f"{self.lat} {self.lon}"