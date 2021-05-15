def simpleCoroutine():
    i = yield
    print("coroutine received {!s}".format(i))

sc = simpleCoroutine()
next(sc)
print("coroutine wailt")
sc.send(11)
# coroutine wailt
# coroutine received 11
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note33\test.py", line 8, in <module>
#     sc.send(11)
# StopIteration