import requests
import os
import sys

# Use environment variable for API key security
# Set with: set OPENWEATHER_API_KEY=your_key_here (Windows) or export OPENWEATHER_API_KEY=your_key_here (Linux/Mac)
API_KEY = os.environ.get('OPENWEATHER_API_KEY', 'ee5ab21cc2405127ff46ebc7add3de6d')

if API_KEY == 'ee5ab21cc2405127ff46ebc7add3de6d':
    print("Warning: Using default API key. Set OPENWEATHER_API_KEY environment variable for production use.\n")


def convert_kelvin_to_celsius(kelvin_temperature):
    """Convert Kelvin to Celsius"""
    return round(kelvin_temperature - 273.15, 2)


def get_weather(city_name):
    """Fetch weather data for a city"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)


def display_weather(city_name):
    """Display weather information for a city"""
    print(f"Fetching weather for {city_name.title()}...\n")
    
    data = get_weather(city_name)
    
    # Extract data
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    feels_like = data['main']['feels_like']
    weather = data['weather'][0]['main']
    weather_desc = data['weather'][0]['description']
    
    # Convert temperatures
    temperatura = convert_kelvin_to_celsius(temp)
    temp_minimum = convert_kelvin_to_celsius(temp_min)
    temp_maximum = convert_kelvin_to_celsius(temp_max)
    feels = convert_kelvin_to_celsius(feels_like)
    
    # Display results
    print("="*50)
    print(f"Location: {city_name.title()}")
    print("="*50)
    print(f"Temperature: {temperatura}°C")
    print(f"Feels like: {feels}°C")
    print(f"Min: {temp_minimum}°C")
    print(f"Max: {temp_maximum}°C")
    print(f"Conditions: {weather} - {weather_desc}")
    print("="*50 + "\n")


if __name__ == "__main__":
    # Allow city name as command line argument
    city = sys.argv[1] if len(sys.argv) > 1 else "milan"
    display_weather(city)

