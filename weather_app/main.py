"""
Weather Checker
----------------
Lets the user check the current weather either by city name
(using geocoding) or by entering coordinates directly.
"""

from weather import get_weather, search_by_city, get_weather_description

while True:
    print("""=== Weather Checker ===
1. Check weather by city name
2. Search by coordinates
3. Exit""")
    
    option = int(input("Choose an option: "))
    
    if option == 1:
        city = input("Enter the city name: ")
        lat, lon = search_by_city(city)
        if lat is not None and lon is not None:
            weather = get_weather(lat, lon)
            print(f"The weather in {city} is: {weather['temperature_2m']}°C, wind speed: {weather['windspeed_10m']} km/h, conditions: {get_weather_description(weather['weathercode'])}")
        else:
            print("Could not get the weather for that city")
        input("\nPress Enter to continue...")
        
    elif option == 2:
        try:
            lat = float(input("Enter the latitude: "))
            lon = float(input("Enter the longitude: "))
            weather = get_weather(lat, lon)
            print(f"The weather at coordinates ({lat}, {lon}) is: {weather['temperature_2m']}°C, wind speed: {weather['windspeed_10m']} km/h, conditions: {get_weather_description(weather['weathercode'])}")
        except ValueError:
            print("Please enter valid values for latitude and longitude.")
        input("\nPress Enter to continue...")
    
    elif option == 3:
        print("Thanks for using the weather checker. Goodbye!")
        break