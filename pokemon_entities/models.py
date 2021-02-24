from django.db import models


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Имя', max_length=200)
    title_en = models.CharField(verbose_name='Имя на английском',
                                max_length=200, blank=True)
    title_jp = models.CharField(verbose_name='Имя на японском', max_length=200,
                                blank=True)
    description = models.TextField(verbose_name='Описание',
                                   default='Описание покемона',
                                   blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='pokemons',
                              null=True, blank=True)
    previous_evolution = models.ForeignKey('Pokemon',
                                           verbose_name='Предыдущая эволюция',
                                           related_name='next_evolutions',
                                           null=True, blank=True,
                                           on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон',
                                related_name='entities',
                                on_delete=models.CASCADE)
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    appeared_at = models.DateTimeField(verbose_name='Появится', null=True)
    disappeared_at = models.DateTimeField(verbose_name='Исчезнет', null=True)
    level = models.IntegerField(verbose_name='Уровень', blank=True)
    health = models.IntegerField(verbose_name='Здоровье', blank=True)
    strength = models.IntegerField(verbose_name='Сила', blank=True)
    defence = models.IntegerField(verbose_name='Защита', blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True)

    def __str__(self):
        return f"{self.lat} {self.lon}"
