"""
Shows how to use __call__ 
"""


class Foo:
    """ Shows how to use __call__ to make an instance callable. """

    def __call__(self, *args, **kwargs) -> str:
        """ This special method allows you to use the instance as if it were a function. """
        print('You called Foo!')
        return 'bar'


x = Foo()
print(x(2, 3))
