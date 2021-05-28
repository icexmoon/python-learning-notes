class TestClass:
    def __init__(self) -> None:
        self.opt1 = 1
        self.opt2 = 2

tc = TestClass()
setattr(tc, 'opt1', 111)
setattr(tc, 'opt3', 333)
print(tc.opt1)
print(tc.opt3)
# 111
# 333