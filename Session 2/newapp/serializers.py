from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        # '__all__' likhne se saare fields (id, name, cuisine, rating, created_at) serialize ho jayenge
        fields = '__all__'

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError("Rating must be between 0.0 and 5.0.")
        return value