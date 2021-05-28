class TestClass:
    def __init__(self) -> None:
        self.__opt1 = 1

    def get_opt1(self):
        return self.__opt1

    def set_opt1(self, value):
        self.__opt1 = value

    def del_opt1(self):
        del self.__opt1
    opt1 = property(fget=get_opt1, fset=set_opt1, fdel=del_opt1)


tc = TestClass()
print(type(TestClass.opt1))
print(tc.opt1)
print(tc.__dict__)
tc.opt1 = 2
print(tc.opt1)
del tc.opt1
print(tc.opt1)
# <class 'property'>
# 1
# {'_TestClass__opt1': 1}
# 2
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 23, in <module>
#     print(tc.opt1)
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 6, in get_opt1
#     return self.__opt1
# AttributeError: 'TestClass' object has no attribute '_TestClass__opt1'
