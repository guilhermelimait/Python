# 🌡️ City Temperature - Weather Information Tool

Get real-time weather information for any city using the OpenWeatherMap API.

## 📝 Description

A Python script that fetches current weather data including temperature, feels-like temperature, min/max temperatures, and weather conditions for any city worldwide.

## ✨ Features

- **Real-Time Weather**: Current temperature and conditions
- **Temperature Conversion**: Automatic Kelvin to Celsius conversion
- **Detailed Information**: Min/max temps, feels-like, weather description
- **Global Coverage**: Works for cities worldwide
- **Easy API Integration**: Simple OpenWeatherMap API usage

## 📋 Prerequisites

- Python 3.8+
- OpenWeatherMap API key (free tier available)
- Internet connection

## 📦 Installation

```bash
# Install required package
pip install requests
```

## 🔑 API Setup

1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
2. Replace the API key in the script:

```python
API_KEY = "your_api_key_here"
```

## 🚀 Usage

### Basic Usage

```bash
python getcitytemp.py
```

### Change City

Edit the `city_name` variable in the script:

```python
city_name = "london"  # Change to your desired city
```

### Example Output

```
A temperatura em milan é 15.32
A sensação térmica é de 14.21
Minimum temperature is: 13.5
Maximum temperature is: 17.0
O clima será de Clouds com scattered clouds
```

## 🔧 Configuration

### Complete Usage Example

```python
import requests

API_KEY = "your_api_key_here"
city_name = "paris"

# Build API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_KEY}"

# Make request
response = requests.get(url).json()

# Extract data
temp = response['main']['temp']
feels = response['main']['feels_like']
weather = response['weather'][0]['main']

# Convert to Celsius
celsius = round(temp - 273.15, 2)
```

## 📊 Available Data

| Field | Description | Unit |
|-------|-------------|------|
| `temp` | Current temperature | Kelvin/Celsius |
| `temp_min` | Minimum temperature | Kelvin/Celsius |
| `temp_max` | Maximum temperature | Kelvin/Celsius |
| `feels_like` | Perceived temperature | Kelvin/Celsius |
| `humidity` | Humidity percentage | % |
| `pressure` | Atmospheric pressure | hPa |
| `weather.main` | Weather condition | Text |
| `weather.description` | Detailed description | Text |

## 💡 Use Cases

- **Travel Planning**: Check weather before trips
- **Daily Updates**: Morning weather routine
- **Weather Monitoring**: Track temperature changes
- **Application Integration**: Add weather to your apps

## 🎯 Advanced Features

### Multiple Cities

```python
cities = ["london", "paris", "tokyo", "new york"]

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}"
    response = requests.get(url).json()
    temp = round(response['main']['temp'] - 273.15, 2)
    print(f"{city}: {temp}°C")
```

### Fahrenheit Conversion

```python
def kelvin_to_fahrenheit(kelvin):
    return round((kelvin - 273.15) * 9/5 + 32, 2)
```

### Get More Data

```python
# Wind information
wind_speed = response['wind']['speed']
wind_direction = response['wind']['deg']

# Humidity and pressure
humidity = response['main']['humidity']
pressure = response['main']['pressure']

# Visibility
visibility = response.get('visibility', 'N/A')

# Sunrise and sunset
sunrise = response['sys']['sunrise']
sunset = response['sys']['sunset']
```

### Error Handling

```python
try:
    response = requests.get(url).json()
    if response.get('cod') != 200:
        print(f"Error: {response.get('message')}")
    else:
        # Process weather data
        pass
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
```

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| requests | 2.31.0+ | HTTP API requests |

## 🐛 Troubleshooting

**Issue**: "Invalid API key"
- Verify your API key is correct
- Check if API key is activated (may take a few minutes)
- Ensure no extra spaces in API_KEY variable

**Issue**: City not found
- Check spelling of city name
- Try adding country code: `"london,uk"`
- Use city ID instead of name

**Issue**: Network error
- Check internet connection
- Verify API endpoint is accessible
- Check firewall settings

## 🌐 API Limitations

Free tier limitations:
- 60 calls per minute
- 1,000,000 calls per month
- Current weather data only

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

**Part of the [Python Projects Collection](../README.md)**
