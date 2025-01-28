"""
Shows how to use __getattribute__ and __getattr__ to intercept attribute access.
"""


class Foo:
    def __init__(self, x: int, y: int):
        self.x = x  # This will call __setattr__
        self.y = y

    def product(self) -> int:
        return self.x * self.y  # This will call __getattribute__

    def __setattr__(self, *args, **kwargs):
        print("in __setattr__", self, args, kwargs)
        super().__setattr__(*args)

    def __getattribute__(self, *args, **kwargs):  # builtin getattr() does NOT send the default
        print("in __getattribute__", self, args, kwargs)
        return super().__getattribute__(*args)

    def __getattr__(self, item):  # There is no super().__getattr__(). object does NOT implement it.
        print("in __getattr__", self, item)
        return "Goodbye"


foo = Foo(2, 3)
print(foo.x)
print(foo.z)
