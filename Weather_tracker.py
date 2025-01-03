import requests

class WeatherTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"
        
    def fetch_weather(self, location):
        url = f"{self.base_url}weather?q={location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                'location': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_info
        else:
            return None
    
    def fetch_forecast(self, location):
        url = f"{self.base_url}forecast?q={location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            forecasts = []
            for entry in data['list'][:5]:  # Fetching the next 5 time slots
                forecast = {
                    'datetime': entry['dt_txt'],
                    'temperature': entry['main']['temp'],
                    'description': entry['weather'][0]['description']
                }
                forecasts.append(forecast)
            return forecasts
        else:
            return None
        
    def fetch_alerts(self, location):
        # Assuming we have access
        url = f"{self.base_url}alerts?q={location}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            alerts = data.get('alerts', [])
            return alerts if alerts else "No weather alerts."
        else:
            return None
        
if __name__ == "__main__":
    api_key = "Replace here with your open weather API KEY"  
    tracker = WeatherTracker(api_key)

    location = input("Enter Location Of your choice. Example (Moscow, London, Dubai, Nairobi): ")

    print("\n--- Current Weather ---")
    weather = tracker.fetch_weather(location)
    if weather:
        print(f"Location: {weather['location']}")
        print(f"Temperature: {weather['temperature']} °C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Could not fetch weather data.")

    print("\n--- Weather Forecast ---")
    forecast = tracker.fetch_forecast(location)
    if forecast:
        for entry in forecast:
            print(f"Date & Time: {entry['datetime']}, Temp: {entry['temperature']} °C, Desc: {entry['description']}")
    else:
        print("Could not fetch forecast data.")

    print("\n--- Weather Alerts ---")
    alerts = tracker.fetch_alerts(location)
    if alerts:
        if isinstance(alerts, str):
            print(alerts)
        else:
            for alert in alerts:
                print(f"Alert: {alert['event']} - {alert['description']}")
    else:
        print("Could not fetch alert data.")