def test_yield():
    print('start')
    yield 1
    print('after')

ty = test_yield()
next(ty)
next(ty)
# start
# after
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note32\test.py", line 8, in <module>
#     next(ty)
# StopIteration