class TestClass:
    def __init__(self) -> None:
        self.__dict__['opt1'] = 1

    @property
    def opt1(self):
        return 42


tc = TestClass()
print(tc.opt1)
del TestClass.opt1
print(tc.opt1)
# 42
# 1