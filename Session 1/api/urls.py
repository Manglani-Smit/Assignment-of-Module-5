from django.urls import path
from . import views

urlpatterns = [
    path('hello_spotify/', views.hello_spotify, name='hello_spotify'),
    path('restaurant/', views.test_restaurant, name='test_restaurant'),
]