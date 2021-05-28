class TestClass:
    def __init__(self) -> None:
        self.opt1 = 1
        self.opt2 = 2

tc = TestClass()
print(getattr(tc,'opt1'))
print(getattr(tc,'opt3',3))
print(getattr(tc,'opt3'))
# 1
# 3
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 9, in <module>
#     print(getattr(tc,'opt3'))
# AttributeError: 'TestClass' object has no attribute 'opt3'