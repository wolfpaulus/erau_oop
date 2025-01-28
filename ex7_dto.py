"""
Using json.loads' object_hook parameter to create a custom object from a JSON string.
object_hook is an optional function that will be called with the result of any object literal decoded (a dict).
"""
import json


class Decoder():
    """ A class that decodes a dictionary into an object. """

    def __init__(self, /, **kwargs):
        self.__dict__.update(kwargs)
        print(repr(self))

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = (f"{k}={self.__dict__[k].__repr__()}" for k in keys)
        return f"({", ".join(items)})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __contains__(self, key):
        return key in self.__dict__

    def __hash__(self):
        return hash(frozenset(self.__dict__.items()))

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)


str_ = {"User": {"Name": "SQWiperYT", "ID": 10, "Other": {"ID": 1}}}

dto = json.loads(json.dumps(str_), object_hook=lambda d: Decoder(**d))
print(dto.User.Name)  # instead of dict_["User"]["Name"]
