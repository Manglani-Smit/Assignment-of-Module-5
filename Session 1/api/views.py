from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RestaurantSerializer
"""
TASK 4: JSON vs XML Comparison
--------------------------------------------------------------------------------
1. JSON (JavaScript Object Notation):
   - Lightweight, human-readable, and faster to parse.
   - Native to JavaScript and standard for modern REST APIs.
   Sample Response (Flipkart Product):
   {
       "product_name": "Wireless Bluetooth Headphones",
       "price": 1499.00
   }

2. XML (eXtensible Markup Language):
   - Tag-based, heavier payload, supports strict schema validation (XSD).
   - Verbose and takes more bandwidth compared to JSON.
   Sample Response (Flipkart Product):
   <product>
       <product_name>Wireless Bluetooth Headphones</product_name>
       <price>1499.00</price>
   </product>
--------------------------------------------------------------------------------
"""

@api_view(['GET'])
def hello_spotify(request):
    data = {
        "message": "Hello, Spotify Fans!"
    }
    return Response(data)

@api_view(['GET'])
def test_restaurant(request):
    sample_restaurant = {
        "name": "Honest Restaurant",
        "cuisine": "Pav Bhaji, Punjabi & Chinese"
    }
    serializer = RestaurantSerializer(sample_restaurant)
    return Response(serializer.data)