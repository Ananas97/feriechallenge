import json
import requests
from program2 import config
from datetime import date


def fetch_weather(city):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.API_KEY}"
    response = requests.get(URL)
    json_data = json.loads(response.text)
    print_now_date()
    print(f'Temperature: {covert_kelvin_to_celcius(json_data["main"]["temp"])}°C')
    print(f'Pressure: {json_data["main"]["pressure"]} hPa')
    print(f'Humidity: {json_data["main"]["humidity"]} %')


def covert_kelvin_to_celcius(kelvin_degrees):
    return round((kelvin_degrees - 273.15))


def print_now_date():
    today = date.today()
    print("Today's date:", today)


if __name__ == "__main__":
    print("Weather checker")
    while True:
        city = str(input("Enter city: "))
        fetch_weather(city)
