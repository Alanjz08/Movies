from django.db import models

# Create your models here.
class Studio(models.Model):
    nombre = models.CharField(max_length=30)

class Pelicula(models.Model):
    genretype = models.TextChoices("genretype","Adventure Drama Sci-fi Comedy Action Terror")
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    country = models.CharField(max_length=64)
    description = models.TextField()
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True)
    genre = models.CharField(blank=False, choices=genretype.choices, max_length=18)
    image = models.URLField()
    