from django.contrib import admin
from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'slug')

admin.site.register(Pet, PetAdmin)
