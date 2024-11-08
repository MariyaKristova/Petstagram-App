from django.contrib import admin

from petstagram_app.pets.models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')