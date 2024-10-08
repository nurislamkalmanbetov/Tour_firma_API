from django.contrib import admin
from .models import Tours


@admin.register(Tours)
class TourAdmin(admin.ModelAdmin):
    list_display = (
        'id','title', 'description', 'created_at',
        'price', 'user',
        )