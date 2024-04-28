from django.contrib import admin
from film.models import *
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'rating',
        'description',
    )