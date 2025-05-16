# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import requests
api_key = "30fe13b10441a95ac90adcc9351e8bfd"  # Replace with your actual API key
api_url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}"
new_url=f"https://api.openweathermap.org/data/3.0/onecall/timemachine"

city = "New York"

# Make the API request
response = requests.get(api_url, params={
    "q": city,
    "appid": api_key,
    "units": "metric"  # Use "metric" for Celsius, "imperial" for Fahrenheit
})

timestamp=1000216980
newresponse = requests.get(api_url, params={
    "q": city,
    "dt": timestamp,
    "appid": api_key,
    "units": "metric"
})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract and print relevant information
    print(data)
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Current temperature in {city} is {temp}°C with {weather}.")
    windspeed=data["wind"]["speed"]
    print(f"current wind speed is {windspeed}.")
else:
    print("Failed to fetch weather data:", response.status_code, response.text)

if newresponse.status_code == 200:
    data = newresponse.json()
    # Extract and print relevant information
    print(data)
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Current temperature in {city} is {temp}°C with {weather}.")
    windspeed = data["wind"]["speed"]
    print(f"current wind speed is {windspeed}.")
   
else:
    print("Failed to fetch weather data:", response.status_code, response.text)
