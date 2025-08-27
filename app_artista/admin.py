from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Artista, Cancion

admin.site.register(Artista)
admin.site.register(Cancion)