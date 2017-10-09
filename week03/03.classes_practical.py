# Task. Class takes name of a city and returns weather forecast for this city
import pprint
import requests
from dateutil.parser import parse

class YahooWeatherForecast:
    def __init__(self):
        self._city_cache = {}


    def get(self,city):

        if city in self._city_cache:
            return self._city_cache[city]

        query = f"https://query.yahooapis.com/v1/public/yql?q=\
        select%20*%20from%20weather.forecast%20where%20woeid%20in%20\
        (select%20woeid%20from%20geo.places(1)%20where%20text%3D'{city}')%20and%20u%3D'c'&format=json"
#        print("Sending HTTP Request...")
        data = requests.get(query).json() # no error catching!
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"] # no error catching!

        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date":parse(day_data["date"]), # no error catching
                "high_temp": day_data["high"]
            })

        self._city_cache[city]=forecast
        return forecast


class CityInfo:
    def __init__(self, name, weather_forecast=None):
        self._weather_forecast = weather_forecast or YahooWeatherForecast()
        self.city = name

    def weather_forecast(self):
        result = self._weather_forecast.get(self.city)
        return result


def _main():
    weather_forecast = YahooWeatherForecast()
    for i in range(5):
        city_info = CityInfo("Murmansk", weather_forecast)
        forecast = city_info.weather_forecast()
        pprint.pprint(forecast)


if __name__ == "__main__":
    _main()
