from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Restaurant
from .serializers import RestaurantSerializer
from .pagination import RestaurantPageNumberPagination, RestaurantLimitOffsetPagination

class RestaurantViewSet(viewsets.ModelViewSet):
    # Base Queryset aur Serializer (Q1)
    queryset = Restaurant.objects.all().order_by('id')
    serializer_class = RestaurantSerializer

    # Question 2: PageNumberPagination set kiya (3 per page)
    # Question 3 test karte time ise switch karke RestaurantLimitOffsetPagination karenge
    pagination_class = RestaurantLimitOffsetPagination

    # Question 4 & Question 5: Backends enable kiye
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    # Question 5: Cuisine field par exact filter
    filterset_fields = ['cuisine']

    # Question 4: Ordering support (name aur cuisine)
    ordering_fields = ['name', 'cuisine']
    ordering = ['name']  # Default ordering by name