from django.contrib import admin
from . import models


@admin.register(models.Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "location", "email")
    search_fields = ("name", "location",)

@admin.register(models.PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("card", "trainer", "collection_date")
    search_fields = ("card", "trainer")