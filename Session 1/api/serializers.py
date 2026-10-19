from rest_framework import serializers

# TASK 5: Basic Serializer for Zomato Restaurant Object
# Prompt used: "Write a basic serializer class in Django REST Framework for a Restaurant object having fields: name and cuisine without connecting to a database model."

class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    cuisine = serializers.CharField(max_length=100)