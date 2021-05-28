class TestCls:
    __slots__=('opt1','opt2')
    def __init__(self) -> None:
        self.opt1 = 1
        self.opt2 = 2

tc = TestCls()
# tc.opt3 = 3
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 8, in <module>
#     tc.opt3 = 3
# AttributeError: 'TestCls' object has no attribute 'opt3'
# print(tc.__dict__)
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 13, in <module>
#     print(tc.__dict__)
# AttributeError: 'TestCls' object has no attribute '__dict__'