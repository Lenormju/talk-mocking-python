from lenormju.meteo_station import MeteoStation, MeteoConfig

CONFIG = MeteoConfig("https://api.openweathermap.org")

METEO_STATION = MeteoStation(CONFIG)

class MeteoApp:
    def should_i_bring_a_jacket(self) -> str:
        temperature = METEO_STATION.get_current_temperature_at_campus_rene_cassin()
        if temperature < 15.0:
            return "Definitely!"
        elif temperature < 22.0:
            return "Probably"
        elif temperature < 25.0:
            return "Just in case ?"
        else:
            return "No need"

METEO_APP = MeteoApp()
