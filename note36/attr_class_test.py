class TestClass:
    def __init__(self) -> None:
        pass

tc = TestClass()
print(tc.__class__)
print(type(tc))
print(tc.__class__ == type(tc))
print(type(tc.__class__))
# <class '__main__.TestClass'>
# <class '__main__.TestClass'>
# True
# <class 'type'>