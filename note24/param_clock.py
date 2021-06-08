import time


def clockWithParam(fmt: str = "[{times:0.8f}s] {name}({argStr})->{result}"):
    def clockDecorator(func):
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
            name = func.__name__
            print(fmt.format(**locals()))
            return result
        return clocked
    return clockDecorator