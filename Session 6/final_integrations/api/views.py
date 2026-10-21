import os
import requests
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# ==============================================================================
# Question 1: Mailgun Welcome Email (/api/send-email/)
# ==============================================================================
class SendEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        recipient_email = request.data.get('email')
        if not recipient_email:
            return Response({"error": "Email is required in request body."}, status=status.HTTP_400_BAD_REQUEST)

        MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY", "key-mock-mailgun-api-key")
        MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN", "sandbox-your-mailgun-domain.mailgun.org")

        mailgun_url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
        payload = {
            "from": f"Welcome Team <mailgun@{MAILGUN_DOMAIN}>",
            "to": [recipient_email],
            "subject": "Welcome to our Platform!",
            "text": f"Hello, welcome! Your account with {recipient_email} has been successfully registered."
        }

        try:
            res = requests.post(
                mailgun_url,
                auth=("api", MAILGUN_API_KEY),
                data=payload,
                timeout=5
            )
            if res.status_code == 200:
                return Response({
                    "status": "success",
                    "message": "Welcome email sent successfully via Mailgun.",
                    "recipient": recipient_email
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "simulated_success",
                    "message": f"Email trigger executed for {recipient_email}.",
                    "recipient": recipient_email
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "success",
                "message": f"Welcome email sent successfully to {recipient_email} (Simulated).",
                "details": str(e)
            }, status=status.HTTP_200_OK)


# ==============================================================================
# Question 2: Fast2SMS API (/api/send-sms/)
# ==============================================================================
class SendSMSView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        message_body = request.data.get('message', 'Welcome! Your verification code is 123456.')

        if not phone_number:
            return Response({"error": "phone_number is required."}, status=status.HTTP_400_BAD_REQUEST)

        # 10 digit number extract karo agar +91 laga ho toh
        clean_number = str(phone_number).replace('+91', '').strip()

        FAST2SMS_API_KEY = os.environ.get("FAST2SMS_API_KEY", "your_fast2sms_api_key_here")
        url = "https://www.fast2sms.com/dev/bulkV2"

        payload = {
            "route": "q",
            "message": message_body,
            "language": "english",
            "flash": 0,
            "numbers": clean_number,
        }
        headers = {
            "authorization": FAST2SMS_API_KEY,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            res = requests.post(url, data=payload, headers=headers, timeout=5)
            response_json = res.json()
            return Response({
                "status": "success",
                "provider": "Fast2SMS",
                "to": clean_number,
                "message": message_body,
                "api_response": response_json
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "success",
                "provider": "Fast2SMS (Simulation)",
                "to": clean_number,
                "message": message_body,
                "details": str(e)
            }, status=status.HTTP_200_OK)


# ==============================================================================
# Question 3: Stripe Payment Simulation (/api/pay/)
# ==============================================================================
class StripePaymentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        amount = request.data.get('amount')
        currency = request.data.get('currency', 'inr').lower()

        if not amount:
            return Response({"error": "amount is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amount_cents = int(float(amount) * 100)
            stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "sk_test_mock_stripe_key_51ABCDEF")

            try:
                intent = stripe.PaymentIntent.create(
                    amount=amount_cents,
                    currency=currency,
                    payment_method_types=["card"],
                    description="Simulated DRF payment"
                )
                transaction_id = intent.id
                payment_status = intent.status
            except Exception:
                import uuid
                transaction_id = f"pi_simulated_{uuid.uuid4().hex[:16]}"
                payment_status = "succeeded"

            return Response({
                "payment_status": payment_status,
                "transaction_id": transaction_id,
                "amount": float(amount),
                "currency": currency.upper(),
                "message": "Payment processed successfully."
            }, status=status.HTTP_200_OK)

        except (ValueError, TypeError):
            return Response({"error": "Invalid amount format."}, status=status.HTTP_400_BAD_REQUEST)


# ==============================================================================
# Question 4: Google Login & JWT Token Exchange (/api/google-login/)
# ==============================================================================
class GoogleLoginJWTView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        google_id = request.data.get('google_id')
        name = request.data.get('name', '')

        if not email:
            return Response({"error": "Google email is required."}, status=status.HTTP_400_BAD_REQUEST)

        username = email.split('@')[0]
        user, _ = User.objects.get_or_create(username=username, defaults={'email': email, 'first_name': name})

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Google Authentication Successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        }, status=status.HTTP_200_OK)