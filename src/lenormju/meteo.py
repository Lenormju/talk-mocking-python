import os

import requests


def get_current_temperature_at_campus_rene_cassin() -> float:
    openweather_api_key = os.environ["OPENWEATHER_API_KEY"]
    campus_rene_cassin_lat_lon = (45.76848080143464, 4.8058961701254175)
    lat, lon = campus_rene_cassin_lat_lon
    # no `mode`  because we want the responses to be in JSON, otherwise "html"/"xml"
    lang = "fr"
    units = "metric"  # "standard"/"metric"/"imperial"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api_key}&lang={lang}&units={units}"
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


def should_i_bring_a_jacket() -> str:
    temperature = get_current_temperature_at_campus_rene_cassin()
    if temperature < 15.0:
        return "Definitely!"
    elif temperature < 22.0:
        return "Probably"
    elif temperature < 25.0:
        return "Just in case ?"
    else:
        return "No need"
