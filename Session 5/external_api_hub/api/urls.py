from django.urls import path
from .views import (
    MusicFestivalWeatherView,
    FoodLocationView,
    CountryInfoView,
    GitHubReposView
)

urlpatterns = [
    # Q1: Weather by city
    path('music-weather/<str:city>/', MusicFestivalWeatherView.as_view(), name='music-weather'),

    # Q2: Food location by restaurant query param (?name=...)
    path('food-location/', FoodLocationView.as_view(), name='food-location'),

    # Q3: Country information
    path('country-info/<str:country_name>/', CountryInfoView.as_view(), name='country-info'),

    # Q4: GitHub repos by username
    path('github-repos/<str:username>/', GitHubReposView.as_view(), name='github-repos'),
]