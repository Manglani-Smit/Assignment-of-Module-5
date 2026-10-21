from django.urls import path
from .views import SendEmailView, SendSMSView, StripePaymentView, GoogleLoginJWTView

urlpatterns = [
    path('send-email/', SendEmailView.as_view(), name='send-email'),
    path('send-sms/', SendSMSView.as_view(), name='send-sms'),
    path('pay/', StripePaymentView.as_view(), name='pay'),
    path('google-login/', GoogleLoginJWTView.as_view(), name='google-login'),
]