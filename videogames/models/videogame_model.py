from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import secrets
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError

from backend.settings import AUTH_USER_MODEL

class Genre(models.Model):
    name = models.CharField(verbose_name="Nombre del genero del juego", null=False, max_length=50,
                            help_text="Solo RPG, Terror y Fantasia")
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        db_table = "genre"
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def clean(self):
        allowed_genres = ["RPG", "Terror", "Fantasia"]
        if self.name not in allowed_genres:
            raise ValidationError(f"El género '{self.name}' no es válido. Opciones permitidas: {', '.join(allowed_genres)}.")

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            cont = 1

            while Genre.objects.filter(slug=slug).exists():
                slug = f"{slug}-{cont}"
                cont += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Videogame(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(max_length=300, verbose_name="Descripción del juego")
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Genero del juego")
    gameImg = models.ImageField(upload_to='contents/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        db_table = "videogame"
        verbose_name = "Videogame"
        verbose_name_plural = "Videogames"

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while Videogame.objects.filter(slug=prov).exists():
                prov = secrets.token_urlsafe(16)
            self.slug = prov
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

