
import inspect


def coroutineDecorator(func):
    import functools
    functools.wraps(func)

    def coroutineWrap(*avgs, **kwAvgs):
        coroutine = func(*avgs, **kwAvgs)
        next(coroutine)
        return coroutine
    return coroutineWrap


@coroutineDecorator
def simpleCoroutine():
    i = yield
    print("receive {!s}".format(i))


sc = simpleCoroutine()
print(inspect.getgeneratorstate(sc))
try:
    sc.send(11)
except StopIteration:
    pass
print(inspect.getgeneratorstate(sc))
