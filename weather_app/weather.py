"""
Weather functions: fetch current weather data and geocode a
city name into coordinates, using the free Open-Meteo API.
"""
import requests

WEATHER_CODES = {
    0: "Clear sky ☀️",
    1: "Mostly clear 🌤️",
    2: "Partly cloudy ⛅",
    3: "Cloudy ☁️",
    61: "Light rain 🌧️",
    80: "Rain showers 🌦️",
}

def get_weather_description(code):
    """Translates a weather code into a human-readable description.

    Args:
        code (int): weather code returned by the API.

    Returns:
        str: description of the weather, or an "unknown code" message
        if the code isn't in WEATHER_CODES.
    """
    if code in WEATHER_CODES:
        return WEATHER_CODES.get(code, f"Code {code}")
    else:
        return f"Unknown weather code: {code}"
    
def get_weather(lat, lon):
    """Fetches the current weather for a given coordinate pair.

    Args:
        lat (float): latitude.
        lon (float): longitude.

    Returns:
        dict: current weather data (temperature, wind speed, weather code).
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,windspeed_10m,weathercode&timezone=auto"
    response = requests.get(url)
    data = response.json()
    return data["current"]

def search_by_city(city):
    """Looks up the coordinates of a city by name.

    Args:
        city (str): name of the city to search for.

    Returns:
        tuple: (latitude, longitude), or (None, None) if not found.
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url)
    data = response.json()
    if "results" in data and len(data["results"]) > 0:
        return data["results"][0]["latitude"], data["results"][0]["longitude"]
    else:
        print("City not found.")
        return None, None