""" A simple class to represent a circle """
from math import pi


class Circle:
    """ Circle class with some attributes and behaviors """

    def __init__(self, radius: float) -> None:
        """ The constructor for a circle, which is defined by its radius.
        Args: radius (float): radius of the circle
        """
        self.radius = radius

    def circumference(self) -> float:
        """ A circle is a simple closed curve that divides the plane into two regions.
        Here we calculate the length of that curve.
        Returns: float: circumference of the circle
        """
        return self.radius * 2 * pi

    def area(self) -> float:
        """ A circle is the shape with the largest area for a given length of perimeter
        Returns: float: surface of the circle
        """
        return self.radius ** 2 * pi

    def __repr__(self) -> str:
        """ The goal of __repr__ is to be unambiguous .. e.g. for logging
        If __str__ is not implemented, __repr__ will be used in its place
        Returns: str: description of this circle
        """
        return f"Instance of {self.__class__.__name__} with a radius of {self.radius}"

    def __str__(self) -> str:
        """ The goal of __str__ is to be readable
        Returns: str: description of this circle
        """
        return f"A circle with a radius of {self.radius}, a circumference of {self.circumference():.3f}, and an area of {self.area():.3f}"

    def __eq__(self, __o: object) -> bool:
        """ Define what equality means for Circles
        Args: __o (object): The other circle to compare this one to.
        Returns: bool: True, if the other circle has the same radius as this one.
        """
        return isinstance(__o, self.__class__) and __o.radius == self.radius


a = Circle(1)
b = Circle(2)
c = Circle(2)
print(a.__repr__())
print(a)
print(a == b)
print(b == c)  # equality
print(b is c)  # identity
