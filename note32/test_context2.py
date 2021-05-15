import contextlib
@contextlib.contextmanager
def test_yield():
    print('start')
    yield 1
    print('after')

with test_yield() as hold:
    print(hold)
    1/0
    print('do something')
# start
# 1
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note32\test.py", line 10, in <module>
#     1/0
# ZeroDivisionError: division by zero