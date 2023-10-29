import requests


def get_weather_data(json_data):
    description_of_weather = json_data['weather'][0]['description']
    temperature = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    weather_details = "The weather is {} with a temperature of {}°C, humidity at {}%, and wind speed of {} m/s.".format(
        description_of_weather, temperature, humidity, wind_speed)
    return weather_details

def get_recommendation(weather_data):
    recommendation = ""
    if "rain" in weather_data.lower():
        recommendation = "Don't forget to take an umbrella with you."
    elif "snow" in weather_data.lower():
        recommendation = "Bundle up and wear warm clothing."
    elif "sun" in weather_data.lower():
        recommendation = "It's going to be a sunny day. Don't forget to apply sunscreen."
    else:
        recommendation = "Enjoy your day!"

    return recommendation

def weather(city):
    api_key = "2d86172af916bbaef8e46e2f84dc3739"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric",
        "appid": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        json_data = response.json()
        if json_data["cod"] == 200:
            weather_details = get_weather_data(json_data)
            recommendation = get_recommendation(weather_details)
            print(weather_details)
            print(recommendation)
            
        else:
            print("Unable to retrieve weather information.")
            
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
       

# Example usage
weather("Vitoria-Gasteiz")
