from django.contrib import admin
from .models import Playlist, Order, CartItem, UserProfile, Ticket

admin.site.register(Playlist)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(UserProfile)
admin.site.register(Ticket)