from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import PlaylistListAPIView, OrderListAPIView, CartAPIView, TicketListAPIView

urlpatterns = [
    # Q1: Basic Auth
    path('playlists/', PlaylistListAPIView.as_view(), name='playlist-list'),

    # Q2: Token Auth & Token generation endpoint
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('orders/', OrderListAPIView.as_view(), name='order-list'),

    # Q3: Session Auth Cart
    path('cart/', CartAPIView.as_view(), name='cart-item'),

    # Q4: Custom Premium Permission
    path('tickets/', TicketListAPIView.as_view(), name='ticket-list'),
]