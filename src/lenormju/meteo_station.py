import os
import requests


class MeteoConfig:
    def __init__(self, meteo_url: str) -> None:
        self.meteo_base_url = meteo_url
        self.meteo_token = os.environ["OPENWEATHER_API_KEY"]


class MeteoStation:
    def __init__(self, meteo_config: MeteoConfig) -> None:
        self.meteo_config = meteo_config

    def get_current_temperature_at_campus_rene_cassin(self) -> float:
        campus_rene_cassin_lat_lon = (45.76848080143464, 4.8058961701254175)
        lat, lon = campus_rene_cassin_lat_lon
        # no `mode`  because we want the responses to be in JSON, otherwise "html"/"xml"
        lang = "fr"
        units = "metric"  # "standard"/"metric"/"imperial"
        url = f"{self.meteo_config.meteo_base_url}/data/2.5/weather?lat={lat}&lon={lon}&appid={self.meteo_config.meteo_token}&lang={lang}&units={units}"
        # cf https://openweathermap.org/current
        response = requests.get(url, timeout=5)  # /!\ only 1000 free API calls per day /!\
        response.raise_for_status()
        # example of "200 OK" response : cf "./example_response.json"
        # may reply differently if we exceed the quota :
        # { "cod": 429,
        # "message": "Your account is temporary blocked due to exceeding of requests limitation of your subscription type.
        # Please choose the proper subscription http://openweathermap.org/price"
        # }
        data = response.json()
        return data["main"]["temp"]
