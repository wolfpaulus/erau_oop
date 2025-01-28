"""
super() is a built-in function that returns a proxy object that represents the parent class of the current class.
"""


class Animal(object):
    """Animal class"""

    def __init__(self, animal_type: str) -> None:
        print('Animal Type:', animal_type)


class Terrestrial(Animal):
    """Terrestrial class"""

    def __init__(self) -> None:
        super().__init__("Terrestrial")
        print('A terrestrial animal live predominantly or entirely on land.')


class Aquatic(Animal):
    """Aquatic class"""

    def __init__(self) -> None:
        super().__init__("Aquatic")
        print('An aquatic animal lives in bodies of water for all or most of its lifetime.')


class Amphibian(Terrestrial, Aquatic):
    """Amphibian class"""

    def __init__(self):
        Terrestrial().__init__()
        Aquatic().__init__()
        print('An amphibians can live on land and in water.')


x = Amphibian()
