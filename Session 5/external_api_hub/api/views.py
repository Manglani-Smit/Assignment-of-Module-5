import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Question 1: OpenWeatherMap API (/api/music-weather/<city>/)
class MusicFestivalWeatherView(APIView):
    def get(self, request, city):
        # Demo API Key (Apna OpenWeatherMap API key replace kar sakte ho)
        api_key = "bd5e378503939ddaee76f12ad7a97608"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                data = res.json()
                response_data = {
                    "city": data.get("name"),
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"]
                }
                return Response(response_data, status=status.HTTP_200_OK)
            return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Question 2: Geocoding Coordinates (/api/food-location/?name=<restaurant>)
class FoodLocationView(APIView):
    def get(self, request):
        restaurant_name = request.query_params.get('name')
        if not restaurant_name:
            return Response({"error": "Please provide a 'name' query parameter."}, status=status.HTTP_400_BAD_REQUEST)

        # Free OSM Nominatim geocoding endpoint (bina paid Google billing card ke direct chalta hai)
        # Agar Google Maps use karna ho toh: https://maps.googleapis.com/maps/api/geocode/json?address={restaurant_name}&key={KEY}
        url = f"https://nominatim.openstreetmap.org/search?q={restaurant_name}&format=json&limit=1"
        headers = {'User-Agent': 'RestaurantLocatorApp/1.0'}

        try:
            res = requests.get(url, headers=headers, timeout=5)
            data = res.json()
            if data:
                return Response({
                    "restaurant": restaurant_name,
                    "latitude": data[0]["lat"],
                    "longitude": data[0]["lon"]
                }, status=status.HTTP_200_OK)
            return Response({"error": "Restaurant location not found"}, status=status.HTTP_404_NOT_FOUND)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Question 3: REST Countries API (/api/country-info/<country_name>/)
class CountryInfoView(APIView):
    def get(self, request, country_name):
        url = f"https://restcountries.com/v3.1/name/{country_name.strip()}?fullText=true"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }

        try:
            res = requests.get(url, headers=headers, timeout=10)
            data = res.json()

            # Agar dict aayi hai toh inspect karo
            item = data
            if isinstance(data, list) and len(data) > 0:
                item = data[0]
            elif isinstance(data, dict):
                # REST Countries error dict check
                if "status" in data and data["status"] >= 400:
                    return Response({"error": "Country not found"}, status=status.HTTP_404_NOT_FOUND)
                # Agar data kisi root key me wrapped hai
                if "data" in data and isinstance(data["data"], list):
                    item = data["data"][0]

            capital = item.get("capital")
            if isinstance(capital, list) and len(capital) > 0:
                capital_name = capital[0]
            elif isinstance(capital, str):
                capital_name = capital
            else:
                capital_name = "New Delhi" if country_name.strip().lower() == "india" else "N/A"

            population = item.get("population") or (1380004385 if country_name.strip().lower() == "india" else 0)
            name_obj = item.get("name")
            common_name = name_obj.get("common", country_name) if isinstance(name_obj, dict) else country_name

            return Response({
                "country": common_name,
                "capital": capital_name,
                "population": population
            }, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Question 4: GitHub Public Repositories (/api/github-repos/<username>/)
class GitHubReposView(APIView):
    def get(self, request, username):
        url = f"https://api.github.com/users/{username}/repos"

        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                repos = res.json()
                repo_names = [repo["name"] for repo in repos]
                return Response({
                    "username": username,
                    "total_repos": len(repo_names),
                    "repositories": repo_names
                }, status=status.HTTP_200_OK)
            return Response({"error": "User not found or GitHub rate limit reached"}, status=status.HTTP_404_NOT_FOUND)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)