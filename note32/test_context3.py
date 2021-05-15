import contextlib
@contextlib.contextmanager
def test_yield():
    print('start')
    try:
        yield 1
    except ZeroDivisionError:
        print('division by zero')
    print('after')

with test_yield() as hold:
    print(hold)
    1/0
    print('do something')
# start
# 1
# division by zero
# after