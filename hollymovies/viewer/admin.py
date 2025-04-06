from django.contrib import admin
from viewer.models import Genre, Movie

# Register your models here.

admin.site.register(Genre)
#admin.site.register(Movie)

class MovieAdmin(admin.ModelAdmin):
  list_display = ("title", "genre", "rating", "description", "released",)

admin.site.register(Movie, MovieAdmin)