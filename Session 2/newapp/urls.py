from django.urls import path
from . import views

urlpatterns = [
    # APIView Routes
    path('api/restaurants/', views.RestaurantListCreate.as_view()),
    path('api/restaurants/<int:pk>/', views.RestaurantDetail.as_view()),

    # Mixins Routes
    path('api/mixins/restaurants/', views.RestaurantMixinListCreate.as_view()),
    path('api/mixins/restaurants/<int:pk>/', views.RestaurantMixinDetail.as_view()),
]