import inspect

def simpleCoroutine():
    print("coroutine start")
    print("coroutine running")
    print("coroutine wait")
    i = yield
    print("coroutine running")

def showCoroutineStatus(coroutine):
    print("coroutine status is {!s}".format(inspect.getgeneratorstate(coroutine)))

sc = simpleCoroutine()
showCoroutineStatus(sc)
print("start coroutine")
next(sc)
showCoroutineStatus(sc)
print("send data to coroutine")
try:
    sc.send(11)
except StopIteration:
    pass
showCoroutineStatus(sc)
# coroutine status is GEN_CREATED
# start coroutine
# coroutine start
# coroutine running
# coroutine wait
# coroutine status is GEN_SUSPENDED
# send data to coroutine
# coroutine running
# coroutine status is GEN_CLOSED