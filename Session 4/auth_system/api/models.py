from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.item_name} - {self.total_amount}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Premium: {self.is_premium}"

class Ticket(models.Model):
    movie_name = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.movie_name} ({self.seat_number})"