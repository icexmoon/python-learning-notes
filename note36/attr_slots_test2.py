class TestCls:
    __slots__=('opt1','opt2','__dict__')
    def __init__(self) -> None:
        self.opt1 = 1
        self.opt2 = 2

tc = TestCls()
tc.opt3 = 3
print(tc.opt3)
print(tc.__dict__)
# 3
# {'opt3': 3}