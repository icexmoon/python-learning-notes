import time
from functools import wraps

def clock(func):
    @wraps(func)
    def clocked(*args, **kwArgs):
        start = time.time()
        result = func(*args, **kwArgs)
        end = time.time()
        times = end - start
        argStr = ''
        if len(args) > 0:
            argStr += ','.join(repr(arg) for arg in args)
        if len(kwArgs) > 0:
            argStr += ','.join("%s:%s" % (key, repr(value))
                               for key, value in kwArgs.items())
        print("[%0.8fs] %s(%s)->%s" %
              (times, func.__name__, argStr, str(result)))
        return result
    return clocked