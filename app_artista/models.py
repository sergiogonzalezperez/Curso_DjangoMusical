from django.db import models

# Create your models here.
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del artista o banda")
    nacionalidad = models.CharField(max_length=100)
    foto_artista = models.ImageField(upload_to='img_artistas/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='canciones')

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"

    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"