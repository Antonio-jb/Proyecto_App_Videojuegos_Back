from django.contrib import admin
from reviews.models import Review

class ReviewAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'user', 'genre', 'date', 'created_at', 'updated_at')
    search_fields = ('name', 'genre')
    list_filter = ('genre', 'title')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    readonly_fields = ('date','created_at', 'updated_at','slug')

admin.site.register(Review, ReviewAdmin)