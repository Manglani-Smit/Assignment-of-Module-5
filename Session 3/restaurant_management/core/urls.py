from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet

# Question 1: DefaultRouter register kiya
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')

urlpatterns = [
    path('', include(router.urls)),
]