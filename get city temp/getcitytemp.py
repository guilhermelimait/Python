from clear_screen import clear
import requests

API_KEY = "ee5ab21cc2405127ff46ebc7add3de6d"
city_name = "Belo Horizonte"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_KEY}"
response = requests.get(url).json()
def convert_kelvin_to_celsius(kelvin_temperature):
    return round(kelvin_temperature - 273.15, 2)

response = requests.get(url).json()
temp = response['main']['temp']
feels = response['main']['feels_like']

temperatura = convert_kelvin_to_celsius(temp)
feelslike = convert_kelvin_to_celsius(feels)
clear()
print("\nA temperatura em", city_name, "é",temperatura,"\nA sensação térmica é de", feelslike, "\n")



print (response)
