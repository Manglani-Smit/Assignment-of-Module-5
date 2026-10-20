from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cuisine', 'rating', 'created_at')
    list_filter = ('cuisine', 'rating')
    search_fields = ('name', 'cuisine')