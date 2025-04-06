from django.db import models
from django.db.models import (DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField)

# Create your models here.

class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

#pentru modelul Movie afisarea e facuta in admin.py
class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

