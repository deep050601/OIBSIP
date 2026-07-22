from dotenv import load_dotenv
import os
import requests

load_dotenv()

api = os.getenv("API_KEY")

while True:
    city_name = input("Enter city name: ").strip()

    if not city_name:
        print("Error: City name cannot be empty.")
    elif city_name.isdigit():
        print("Error: City name cannot be only numbers.")
    else:
        break


url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}&units=metric"

try:
    response = requests.get(url,timeout=5)
    if response.status_code == 200:
        data = response.json()

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9 / 5) + 32

        print(f"City name: {data['name']}")
        print("Weather: ", data["weather"][0]["main"])
        print("weather condition: ", data["weather"][0]["description"])
        print(f"Temperature: {temp_c:.1f}°C")
        print(f"Temperature: {temp_f:.1f}°F")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    elif response.status_code == 404:
        print("city not found.")
    elif response.status_code == 401:
        print("invalid api key.")
    else:
      print("Error:", response.status_code)
except requests.exceptions.Timeout:
    print("Request time out.")

except requests.exceptions.ConnectionError:
    print("No internet connection.")

except Exception as e:
    print(e)
