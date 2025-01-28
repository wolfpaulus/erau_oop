""" 
This module is a simple example of how to use __getattr__ and __setattr__ to create a simple lazy weather API client.
Author: Wolf Paulus (https://wolfpaulus.com)
"""
from typing import Any
from urllib.request import urlopen
from json import loads


class Weather:
    """ A class that provides weather information for a few cities in Arizona. """
    cities = {"phoenix": "PSR/158,65", "sedona": "FGZ/64,75", "prescott": "FGZ/39,66", "flagstaff": "FGZ/69,89"}

    def __setattr__(self, name: str, value: Any) -> None:
        """ This method is called when an attribute assignment is attempted. """
        print("setting attribute")
        super().__setattr__(name, value)

    def __getattr__(self, item):
        """ This method is called when an attribute lookup fails. """
        if item in self.__class__.cities:  # in operator when used with dicts, only checks the keys
            URL = f"https://api.weather.gov/gridpoints/{self.__class__.cities[item]}/forecast"
            print("calling API")
            data = loads(urlopen(URL).read())
            self.__setattr__(item, data['properties']['periods'][0]['detailedForecast'])
            # self.__dict__[item] = f"{data['properties']['periods'][0]['detailedForecast']}"
            return self.__dict__[item]


w = Weather()
print(w.sedona)
print(w.prescott)
print(w.sedona)
