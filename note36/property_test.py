class TestClass:
    def __init__(self) -> None:
        self.__opt1 = 1

    @property
    def opt1(self):
        return self.__opt1


tc = TestClass()
print(tc.opt1)
print(tc.__dict__)
tc.opt1 = 2
# 1
# {'_TestClass__opt1': 1}
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 13, in <module>
#     tc.opt1 = 2
# AttributeError: can't set attribute
