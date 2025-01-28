"""
Dataclasses for the NWS API response
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Union, List
from datetime import datetime


@dataclass
class Forecast:
    type: str
    geometry: Geometry
    properties: Properties


@dataclass
class Context:
    wx: str
    geo: str
    unit: str


@dataclass
class Geometry:
    type: str
    coordinates: List[List[List[float]]]


@dataclass
class Properties:
    units: str
    forecastGenerator: str
    generatedAt: datetime
    updateTime: datetime
    validTimes: datetime
    elevation: ProbabilityOfPrecipitationOrElevation
    periods: List[Period]


@dataclass
class ProbabilityOfPrecipitationOrElevation:
    unitCode: str
    value: Union[float, None]


@dataclass
class Period:
    number: int
    name: str
    startTime: datetime
    endTime: datetime
    isDaytime: bool
    temperature: int
    temperatureUnit: str
    temperatureTrend: str
    probabilityOfPrecipitation: ProbabilityOfPrecipitationOrElevation
    windSpeed: str
    windDirection: str
    icon: str
    shortForecast: str
    detailedForecast: str

# 💡 Starting from Python 3.10 (PEP 604), `Union[A, B]` can be simplified as `A | B`
