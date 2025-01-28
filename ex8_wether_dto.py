"""
Compares two ways of parsing JSON data, one using a dictionary and the other using a custom data object.
Author: Wolf Paulus (https://wolfpaulus.com)
"""

from urllib.request import urlopen
from json import loads


# dict parsing

URL = "https://api.weather.gov/gridpoints/FGZ/67,74/forecast?units=us"
with urlopen(URL) as response:
    data = loads(response.read())

assert data is not None and type(data) == dict
forecast = data.get("properties").get("periods")
details = [x.get("detailedForecast") for x in forecast]
print(f"Fetched {len(details)} records. Here is the 1st:\n{details[0]}")


# creating a custom data object from a JSON string

class Forecast:
    def __init__(self, /, **kwargs):  # after /, all arguments are keyword-only
        self.__dict__.update(kwargs)

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


URL = "https://api.weather.gov/gridpoints/FGZ/67,74/forecast?units=us"
with urlopen(URL) as response:
    dto = loads(response.read(), object_hook=lambda d: Forecast(**d))

forecast = dto.properties.periods
details = [x.detailedForecast for x in forecast]
print(f"Fetched {len(details)} records. Here is the 1st:\n{details[0]}")
