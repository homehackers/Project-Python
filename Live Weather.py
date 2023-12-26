import requests

api_key = "93d63f4880fc3e76bf8444af6cff387d"
city = input("Enter your City: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("Raw Weather Data:")
print(data)

temperature = data['main']['temp']
weather_description = data['weather'][0]['description']
humidity = data['main']['humidity']

print("\nWeather Information:")
print(f"Temperature: {temperature}°C")
print(f"Weather: {weather_description}")
print(f"Humidity: {humidity}%")
