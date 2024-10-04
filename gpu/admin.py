from django.contrib import admin
from .models import Gpu

@admin.register(Gpu)
class VinylRecordAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "release_date", "image", "description")

