from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField()
    url = models.URLField()

class Reseña(models.Model):
    autor = models.Charfield(max_length=200)
    descripcion = models.TextField()
    rating = models