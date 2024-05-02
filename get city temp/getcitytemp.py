#from clear_screen import clear
import requests

API_KEY = "ee5ab21cc2405127ff46ebc7add3de6d"
city_name = "milan"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_KEY}"
response = requests.get(url).json()
def convert_kelvin_to_celsius(kelvin_temperature):
    return round(kelvin_temperature - 273.15, 2)

response = requests.get(url).json()
temp = response['main']['temp']
tempmin = response ['main']['temp_min']
tempmax = response ['main']['temp_max']
feels = response['main']['feels_like']
weather = response['weather'][0]['main']
weather2 = response['weather'][0]['description']

temperatura = convert_kelvin_to_celsius(temp)
temp_min = convert_kelvin_to_celsius(tempmin)
temp_max = convert_kelvin_to_celsius(tempmax)
feelslike = convert_kelvin_to_celsius(feels)
#clear()
print("\nA temperatura em", city_name, "é",temperatura,"\nA sensação térmica é de", feelslike)
print("Minimun temperature is:",temp_min)
print("Maximun temperature is:",temp_max)
print("O clima será de", weather, "com", weather2,"\n")

