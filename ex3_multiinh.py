"""
    Multiple Inheritance in Python the diamond of death
"""


class A:
    def __init__(self):
        print("A.__init__")


class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()


class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D.__init__")
        B.__init__(self)
        C.__init__(self)


d = D()
