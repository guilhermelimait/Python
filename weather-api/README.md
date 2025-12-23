def kelvin_to_fahrenheit(kelvin):
# City Temperature - Weather Information Tool

Get real-time weather information for any city using the OpenWeatherMap API.

## Description

Python script that fetches current weather data (temperature, feels-like, min/max, description) for any city.

## Features

- Real-time current conditions
- Kelvin to Celsius conversion
- Min/max and feels-like values
- CLI city override (`python getcitytemp.py london`)
- Environment-based API key

## Prerequisites

- Python 3.8+
- OpenWeatherMap API key
- Internet connection

## Installation

```bash
pip install requests
```

## API Setup

Set your key via environment variable (recommended):

```bash
# Windows
set OPENWEATHER_API_KEY=your_key_here

# Linux/macOS
export OPENWEATHER_API_KEY=your_key_here
```

If the variable is missing, the script warns and uses the placeholder key.

## Usage

```bash
# Default city (Milan)
python getcitytemp.py

# Specify city
python getcitytemp.py "new york"
```

Output shows location, temperature, feels-like, min/max, and conditions.

## Error Handling

- Network/API failures exit with a clear error message.
- Non-200 responses raise exceptions via `response.raise_for_status()`.

## Dependencies

| Package  | Purpose              |
|----------|----------------------|
| requests | HTTP API requests    |

## Notes

- Uses Celsius conversion from Kelvin returned by the API.
- Keep your API key out of source control; use environment variables.

---

Part of the [Python Projects Collection](../README.md)
