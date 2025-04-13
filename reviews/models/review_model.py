from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import secrets

from backend.settings import AUTH_USER_MODEL
from videogames.models.videogame_model import Genre


class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='reviews',
                              verbose_name="Usuario", null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Seleccione el genero del juego")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stars = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        db_table = "reviews"
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while Review.objects.filter(slug=prov).exists():
                prov = secrets.token_urlsafe(16)
            self.slug = prov
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title