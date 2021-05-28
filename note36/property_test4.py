def propertyFactory(name):
    def getter(instance):
        return instance.__dict__[name]

    def setter(instance, value):
        if value > 0:
            instance.__dict__[name] = value
        else:
            raise ValueError("value must > 0")

    def deleter(instance):
        del instance.__dict__[name]
    return property(fget=getter, fset=setter, fdel=deleter)


class TestClass:
    opt1 = propertyFactory("opt1")
    opt2 = propertyFactory("opt2")
    opt3 = propertyFactory("opt3")

    def __init__(self, opt1, opt2, opt3) -> None:
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3

    def __str__(self) -> str:
        return str((self.opt1, self.opt2, self.opt3))


tc1 = TestClass(1, 2, 3)
print(tc1)
tc2 = TestClass(0, 1, 0)
# (1, 2, 3)
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 32, in <module>
#     tc2 = TestClass(0, 1, 0)
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 22, in __init__
#     self.opt1 = opt1
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 9, in setter
#     raise ValueError("value must > 0")
# ValueError: value must > 0