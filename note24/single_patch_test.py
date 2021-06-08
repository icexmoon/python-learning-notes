import numbers
import inspect


def showEverything(obj):
    if isinstance(obj, numbers.Integral):
        print('this is a integer:%s' % obj)
    elif inspect.isfunction(obj):
        sig = inspect.signature(obj)
        argStr = ','.join(name for name, param in sig.parameters.items())
        # result = obj()
        print('this is a function: %s(%s)' % (obj.__name__, argStr))
    elif isinstance(obj, str):
        print('this is a string:%s' % obj)
    else:
        print('this is a object:%r' % obj)


showEverything(1)
showEverything('hellow wolrd!')
showEverything(len)