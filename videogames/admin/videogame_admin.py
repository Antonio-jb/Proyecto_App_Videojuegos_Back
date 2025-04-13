from django.contrib import admin
from videogames.models import Videogame, Genre

class VideogameAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'genre', 'score', 'created_at', 'updated_at')
    search_fields = ('name', 'genre')
    list_filter = ('genre', 'title')
    ordering = ('id',)
    date_hierarchy = 'created_at'

    readonly_fields = ('created_at', 'updated_at','slug')

admin.site.register(Videogame, VideogameAdmin)

class GenreAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name',)
    ordering = ('id',)

    readonly_fields = ('id', 'slug')

admin.site.register(Genre, GenreAdmin)