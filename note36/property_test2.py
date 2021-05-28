class TestClass:
    def __init__(self) -> None:
        self.__opt1 = 1

    @property
    def opt1(self):
        return self.__opt1

    @opt1.setter
    def opt1(self, value):
        self.__opt1 = value

    @opt1.deleter
    def opt1(self):
        del self.__opt1


tc = TestClass()
print(tc.opt1)
print(tc.__dict__)
tc.opt1 = 2
print(tc.opt1)
del tc.opt1
print(tc.opt1)
# 1
# {'_TestClass__opt1': 1}
# 2
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 24, in <module>
#     print(tc.opt1)
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 7, in opt1
#     return self.__opt1
# AttributeError: 'TestClass' object has no attribute '_TestClass__opt1'